import os
import sys
import json
import hashlib
from pathlib import Path
from typing import Any, Dict, Optional
import re

import requests
import yaml


TARGET_LANGS = [
    x.strip().lower()
    for x in os.getenv("TARGET_LANGUAGES", "en").split(",")
    if x.strip()
]

DEEPL_KEY = os.getenv("DEEPL_API_KEY")
CACHE_DIR = Path(".i18n_cache")
CACHE_DIR.mkdir(exist_ok=True)
CACHE_FILE = CACHE_DIR / "translation_cache.json"
CHANGED_CACHE_FILE = CACHE_DIR / "changed_files.json"

# Chunk size for splitting long texts
CHUNK_SIZE = 400
OVERLAP = 50  # Overlap between chunks to preserve context


def load_json_cache(path: Path) -> dict:
    """Load JSON cache safely; return empty dict for missing/empty/invalid files."""
    if not path.exists():
        return {}

    try:
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            return {}

        data = json.loads(raw)
        if isinstance(data, dict):
            return data

        print(f"Warning: Cache file {path} does not contain a JSON object, resetting.")
        return {}
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: Could not read cache file {path}: {e}. Resetting.")
        return {}


CACHE = load_json_cache(CACHE_FILE)
CHANGED_FILES_CACHE = load_json_cache(CHANGED_CACHE_FILE)

# Translation services
TRANSLATION_CACHE = {}


def cache_key(text: str, lang: str) -> str:
    return hashlib.sha256((text + lang).encode()).hexdigest()


def save_cache():
    CACHE_FILE.write_text(json.dumps(CACHE, indent=2, ensure_ascii=False), encoding="utf-8")
    CHANGED_CACHE_FILE.write_text(json.dumps(CHANGED_FILES_CACHE, indent=2, ensure_ascii=False), encoding="utf-8")


def split_into_chunks(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    """Split text into chunks with overlap to preserve context."""
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Move start position, accounting for overlap
        start = end - overlap if end < len(text) else end
    
    return chunks


def deepl_translate(text: str, lang: str) -> Optional[str]:
    """Translate using DeepL API."""
    if not DEEPL_KEY:
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

        if r.status_code == 429:  # Rate limited
            return None

        r.raise_for_status()
        return r.json()["translations"][0]["text"]
    except Exception as e:
        print(f"DeepL error: {e}")
        return None


def google_translate_fallback(text: str, lang: str) -> Optional[str]:
    """Fallback: Free MyMemory API with chunk support (no key needed)."""
    try:
        lang_map = {
            "en": "en",
            "fr": "fr",
            "es": "es",
            "it": "it",
            "pt": "pt",
            "nl": "nl",
            "pl": "pl",
            "ru": "ru",
            "ja": "ja",
            "zh": "zh-CN",
            "de": "de",
        }

        target = lang_map.get(lang.lower(), lang.lower())

        # For long texts, split into chunks
        if len(text) > 500:
            chunks = split_into_chunks(text, chunk_size=400)
            translated_chunks = []
            
            for chunk in chunks:
                # MyMemory free API
                api_url = "https://api.mymemory.translated.net/get"
                params = {
                    "q": chunk,
                    "langpair": f"de|{target}",
                }

                r = requests.get(api_url, params=params, timeout=15)
                r.raise_for_status()

                data = r.json()
                status = data.get("responseStatus")

                if status == 200:
                    translated = data.get("responseData", {}).get("translatedText", "")
                    if translated and translated.strip():
                        translated_chunks.append(translated)
                    else:
                        print(f"Fallback: Empty response from MyMemory (lang: {lang})")
                        return None
                else:
                    print(f"Fallback: MyMemory returned status {status} (lang: {lang})")
                    return None
            
            # Merge chunks and remove duplicate overlap
            result = ""
            for i, chunk in enumerate(translated_chunks):
                if i == 0:
                    result = chunk
                else:
                    # Remove overlapping part from previous chunk
                    if len(result) > OVERLAP:
                        result = result[:-OVERLAP] + chunk
                    else:
                        result += chunk
            
            return result if result.strip() else None
        else:
            # For short texts, translate directly
            api_url = "https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": f"de|{target}",
            }

            r = requests.get(api_url, params=params, timeout=15)
            r.raise_for_status()

            data = r.json()
            status = data.get("responseStatus")

            if status == 200:
                translated = data.get("responseData", {}).get("translatedText", "")
                if translated and translated.strip():
                    return translated
                else:
                    print(f"Fallback: Empty response from MyMemory (lang: {lang})")
                    return None
            else:
                print(f"Fallback: MyMemory returned status {status} (lang: {lang})")
                return None

    except requests.exceptions.Timeout:
        print(f"Fallback: API timeout (lang: {lang})")
    except requests.exceptions.RequestException as e:
        print(f"Fallback: Network error - {e}")
    except Exception as e:
        print(f"Fallback: Unexpected error - {e}")

    return None


def translate_service(text: str, lang: str) -> str:
    """Try DeepL first, fallback to free service with chunks."""
    if not isinstance(text, str) or not text.strip():
        return text

    k = cache_key(text, lang)

    # Check local cache first
    if k in CACHE:
        return CACHE[k]

    # Try DeepL
    if DEEPL_KEY:
        result = deepl_translate(text, lang)
        if result:
            CACHE[k] = result
            return result

    # Fallback to free translation with chunk support
    result = google_translate_fallback(text, lang)
    if result:
        CACHE[k] = result
        return result

    # If all else fails, return original text
    print(f"Warning: Could not translate text, returning original (lang: {lang})")
    return text


def walk(obj: Any, lang: str) -> Any:
    """Recursively translate all strings in an object."""
    if isinstance(obj, str):
        return translate_service(obj, lang)

    if isinstance(obj, dict):
        return {k: walk(v, lang) for k, v in obj.items()}

    if isinstance(obj, list):
        return [walk(i, lang) for i in obj]

    return obj


def translate_yaml(src: Path, lang: str) -> Path:
    """Translate YAML file."""
    data = yaml.safe_load(src.read_text(encoding="utf-8"))
    out = walk(data, lang)
    dst = src.parent / f"{lang}{src.suffix}"

    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False)

    return dst


def translate_json(src: Path, lang: str) -> Path:
    """Translate JSON file."""
    data = json.loads(src.read_text(encoding="utf-8"))
    out = walk(data, lang)
    dst = src.parent / f"{lang}.json"

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    return dst


def translate_md(src: Path, lang: str) -> Path:
    """Translate Markdown file."""
    text = src.read_text(encoding="utf-8")
    out = translate_service(text, lang)
    dst = src.with_name(f"{src.stem}.{lang}.md")
    dst.write_text(out, encoding="utf-8")

    return dst


def process_file(file: Path) -> list[Path]:
    """Process a single file and return generated translation files."""
    generated = []

    for lang in TARGET_LANGS:
        if lang == "de":  # Skip German, it's the source
            continue

        try:
            if file.name in ("README.md", "DOCS.md"):
                dst = translate_md(file, lang)
                generated.append(dst)

            elif file.name in ("de.yaml", "de.yml"):
                dst = translate_yaml(file, lang)
                generated.append(dst)

            elif file.name == "de.json":
                dst = translate_json(file, lang)
                generated.append(dst)
        except Exception as e:
            print(f"Error processing {file} to {lang}: {e}")

    return generated


def get_changed_files() -> list[Path]:
    """Get files changed compared to main."""
    try:
        import subprocess

        # Get the diff between current branch and origin/main
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )

        changed = [
            Path(x.strip())
            for x in result.stdout.splitlines()
            if x.strip()
        ]

        return changed
    except Exception as e:
        print(f"Warning: Could not get changed files: {e}")
        return []


def get_all_files() -> list[Path]:
    """Get all files that should be translated."""
    files = []
    
    # Find all README.md and DOCS.md files
    for pattern in ["README.md", "DOCS.md", "apps/**/README.md", "apps/**/DOCS.md"]:
        files.extend(Path(".").glob(pattern))
    
    # Find all de.yaml, de.yml, de.json files
    for pattern in ["apps/**/translations/de.yaml", "apps/**/translations/de.yml", "apps/**/translations/de.json"]:
        files.extend(Path(".").glob(pattern))
    
    # Remove duplicates and filter valid files
    files = list(set(f for f in files if f.exists()))
    
    return sorted(files)


def should_process_file(file: Path) -> bool:
    """Check if file should be processed."""
    name = file.name

    if name in ("README.md", "DOCS.md"):
        return True

    if name in ("de.yaml", "de.yml", "de.json"):
        return True

    if name.startswith("README_") and name.endswith(".md"):
        return True

    if name.startswith("DOCS_") and name.endswith(".md"):
        return True

    return False


def main():
    """Main translation workflow."""

    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            # Translate all files
            print("Translating ALL files...")
            files = get_all_files()
        else:
            # Use provided file list
            input_file = Path(sys.argv[1])
            files = [
                Path(x.strip())
                for x in input_file.read_text().splitlines()
                if x.strip() and Path(x.strip()).exists()
            ]
    else:
        # Get changed files
        files = get_changed_files()

    if not files:
        print("No files to process")
        return

    print(f"Processing {len(files)} files")

    all_generated = []

    for f in files:
        if should_process_file(f):
            print(f"Translating {f}")
            generated = process_file(f)
            all_generated.extend(generated)
        else:
            print(f"Skipping {f}")

    save_cache()

    print(f"Generated {len(all_generated)} translation files:")
    for f in all_generated:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
