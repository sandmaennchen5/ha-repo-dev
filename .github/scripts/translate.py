#!/usr/bin/env python3
"""Translation script for maintaining multi-language documentation."""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from typing import Any, Dict, Optional, List

import requests
import yaml


# Config
TARGET_LANGS = [
    x.strip().lower()
    for x in os.getenv("TARGET_LANGUAGES", "en").split(",")
    if x.strip()
]

DEEPL_KEY = os.getenv("DEEPL_API_KEY", "").strip()
CACHE_DIR = Path(".i18n_cache")
CACHE_DIR.mkdir(exist_ok=True)
CACHE_FILE = CACHE_DIR / "translation_cache.json"
MANIFEST_FILE = CACHE_DIR / "translation_manifest.json"

# Patterns for files to translate
FILE_PATTERNS = {
    "docs": [
        "README.md",
        "DOCS.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
    ],
    "docs_prefixed": [r"README_\w+\.md", r"DOCS_\w+\.md"],
    "translations": [
        "de.yaml",
        "de.yml",
        "de.json",
    ],
}


def load_cache() -> Dict[str, str]:
    """Load translation cache safely."""
    if not CACHE_FILE.exists():
        return {}

    try:
        raw = CACHE_FILE.read_text(encoding="utf-8").strip()
        if not raw:
            return {}
        data = json.loads(raw)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠ Cache load error: {e}. Starting fresh.")
        return {}


def save_cache(cache: Dict[str, str]):
    """Save translation cache."""
    CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def load_manifest() -> Dict[str, List[str]]:
    """Load previous translation manifest."""
    if not MANIFEST_FILE.exists():
        return {}
    try:
        return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_manifest(manifest: Dict[str, List[str]]):
    """Save translation manifest."""
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def cache_key(text: str, lang: str) -> str:
    """Generate cache key for text+language."""
    return hashlib.sha256((text + "|" + lang).encode()).hexdigest()


def deepl_translate(text: str, lang: str) -> Optional[str]:
    """Translate using DeepL API."""
    if not DEEPL_KEY or not text.strip():
        return None

    try:
        r = requests.post(
            "https://api-free.deepl.com/v2/translate",
            headers={
                "Authorization": f"DeepL-Auth-Key {DEEPL_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "text": [text],
                "source_lang": "DE",
                "target_lang": lang.upper(),
            },
            timeout=30,
        )

        if r.status_code == 429:
            print(f"⚠ DeepL rate limited")
            return None

        r.raise_for_status()
        return r.json()["translations"][0]["text"]
    except Exception as e:
        print(f"✗ DeepL error: {e}")
        return None


def fallback_translate(text: str, lang: str) -> Optional[str]:
    """Fallback: Free MyMemory API."""
    if not text.strip():
        return None

    lang_map = {
        "en": "en", "fr": "fr", "es": "es", "it": "it", "pt": "pt",
        "nl": "nl", "pl": "pl", "ru": "ru", "ja": "ja", "zh": "zh-CN",
        "de": "de",
    }

    try:
        target = lang_map.get(lang.lower(), lang.lower())
        r = requests.get(
            "https://api.mymemory.translated.net/get",
            params={
                "q": text[:500],
                "langpair": f"de|{target}",
            },
            timeout=15,
        )
        r.raise_for_status()

        data = r.json()
        if data.get("responseStatus") == 200:
            result = data.get("responseData", {}).get("translatedText", "")
            return result if result and result.strip() else None

    except requests.exceptions.Timeout:
        print(f"⚠ Fallback timeout (lang: {lang})")
    except Exception as e:
        print(f"⚠ Fallback error: {e}")

    return None


def translate(text: str, lang: str, cache: Dict[str, str]) -> str:
    """Translate text, checking cache first."""
    if not isinstance(text, str) or not text.strip():
        return text

    k = cache_key(text, lang)

    if k in cache:
        return cache[k]

    # Try DeepL first
    if DEEPL_KEY:
        result = deepl_translate(text, lang)
        if result:
            cache[k] = result
            return result

    # Fallback to free service
    result = fallback_translate(text, lang)
    if result:
        cache[k] = result
        return result

    print(f"⚠ No translation for {lang}, using original")
    return text


def walk_translate(obj: Any, lang: str, cache: Dict[str, str]) -> Any:
    """Recursively translate all strings in object."""
    if isinstance(obj, str):
        return translate(obj, lang, cache)

    if isinstance(obj, dict):
        return {k: walk_translate(v, lang, cache) for k, v in obj.items()}

    if isinstance(obj, list):
        return [walk_translate(i, lang, cache) for i in obj]

    return obj


def translate_yaml_file(src: Path, lang: str, cache: Dict[str, str]) -> Optional[Path]:
    """Translate YAML file."""
    try:
        data = yaml.safe_load(src.read_text(encoding="utf-8"))
        out = walk_translate(data, lang, cache)

        # Keep same extension (yaml or yml)
        ext = src.suffix
        dst = src.parent / f"{lang}{ext}"

        with open(dst, "w", encoding="utf-8") as f:
            yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False)

        return dst
    except Exception as e:
        print(f"✗ YAML translation failed {src}: {e}")
        return None


def translate_json_file(src: Path, lang: str, cache: Dict[str, str]) -> Optional[Path]:
    """Translate JSON file."""
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
        out = walk_translate(data, lang, cache)
        dst = src.parent / f"{lang}.json"

        with open(dst, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)

        return dst
    except Exception as e:
        print(f"✗ JSON translation failed {src}: {e}")
        return None


def translate_markdown_file(src: Path, lang: str, cache: Dict[str, str]) -> Optional[Path]:
    """Translate Markdown file."""
    try:
        text = src.read_text(encoding="utf-8")
        out = translate(text, lang, cache)
        dst = src.with_stem(f"{src.stem}.{lang}")

        dst.write_text(out, encoding="utf-8")
        return dst
    except Exception as e:
        print(f"✗ Markdown translation failed {src}: {e}")
        return None


def should_translate(file: Path) -> bool:
    """Check if file should be translated."""
    name = file.name

    # Markdown files
    if name in FILE_PATTERNS["docs"]:
        return True
    if name.endswith(".md"):
        for pattern in FILE_PATTERNS["docs_prefixed"]:
            if __import__("re").match(pattern, name):
                return True

    # Config files
    if name in FILE_PATTERNS["translations"]:
        return True

    return False


def find_files_to_translate(translate_all: bool, changed_files_path: Optional[str] = None) -> List[Path]:
    """Find files to translate."""
    files = []

    if translate_all:
        print("🔍 Scanning all files...")
        for root, dirs, filenames in os.walk("."):
            # Skip hidden dirs
            dirs[:] = [d for d in dirs if not d.startswith(".")]

            for fname in filenames:
                fpath = Path(root) / fname
                if should_translate(fpath) and not fpath.as_posix().startswith(".i18n_cache"):
                    files.append(fpath)
    else:
        print(f"📋 Reading changed files from {changed_files_path}...")
        if changed_files_path and Path(changed_files_path).exists():
            for line in Path(changed_files_path).read_text().splitlines():
                line = line.strip()
                if line and Path(line).exists() and should_translate(Path(line)):
                    files.append(Path(line))

    return files


def process_file(file: Path, cache: Dict[str, str]) -> List[Path]:
    """Translate a single file to all target languages."""
    generated = []

    for lang in TARGET_LANGS:
        if lang == "de":
            continue

        try:
            if file.suffix in (".md",):
                dst = translate_markdown_file(file, lang, cache)
            elif file.suffix in (".yml", ".yaml"):
                dst = translate_yaml_file(file, lang, cache)
            elif file.suffix == ".json":
                dst = translate_json_file(file, lang, cache)
            else:
                continue

            if dst:
                generated.append(dst)
                print(f"  ✓ {file.name} → {dst.name}")
        except Exception as e:
            print(f"  ✗ Error: {e}")

    return generated


def main():
    """Main translation workflow."""
    parser = argparse.ArgumentParser(description="Translate German files to multiple languages")
    parser.add_argument("--all", action="store_true", help="Translate all files (ignore change detection)")
    parser.add_argument("files", nargs="?", help="File with list of changed files (one per line)")

    args = parser.parse_args()

    # Load cache and manifest
    cache = load_cache()
    manifest = load_manifest()
    print(f"📦 Loaded cache with {len(cache)} entries")
    print(f"📋 Loaded manifest with {len(manifest)} source files")

    # Find files to translate
    files = find_files_to_translate(args.all, args.files)

    if not files:
        print("ℹ No files to translate")
        save_cache(cache)
        return

    print(f"\n🌍 Processing {len(files)} file(s)...\n")

    all_generated = []
    manifest_new = {}

    for f in files:
        print(f"📝 {f}")
        generated = process_file(f, cache)
        all_generated.extend(generated)

        # Track generated files in manifest
        src_key = str(f)
        manifest_new[src_key] = [str(g) for g in generated]

    # Save cache and manifest
    save_cache(cache)
    save_manifest(manifest_new)

    print(f"\n✅ Done! Generated {len(all_generated)} translations")
    print(f"📦 Cache saved with {len(cache)} entries")
    print(f"📋 Manifest saved with {len(manifest_new)} source files")

    # Output generated files for GitHub Actions
    print("\n📄 Generated files:")
    for f in all_generated:
        print(f"  - {f}")

    # Write to file for workflow to pick up
    manifest_file = Path(".i18n_cache/generated_files.txt")
    manifest_file.write_text("\n".join(str(f) for f in all_generated), encoding="utf-8")
    print(f"\n✅ File list written to {manifest_file}")


if __name__ == "__main__":
    main()
