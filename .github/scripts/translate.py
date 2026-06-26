import os
import sys
import json
import hashlib
from pathlib import Path

import requests
import yaml


TARGET_LANGS = [
    x.strip().lower()
    for x in os.getenv("TARGET_LANGUAGES", "en").split(",")
    if x.strip()
]

DEEPL_KEY = os.getenv("DEEPL_API_KEY")

if not DEEPL_KEY:
    raise RuntimeError("DEEPL_API_KEY missing")

CACHE_FILE = Path(".translation_cache.json")
CACHE = json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}


def cache_key(text, lang):
    return hashlib.sha256((text + lang).encode()).hexdigest()


def save_cache():
    CACHE_FILE.write_text(json.dumps(CACHE, indent=2, ensure_ascii=False))


def deepl_translate(text, lang):

    k = cache_key(text, lang)

    if k in CACHE:
        return CACHE[k]

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
        timeout=120,
    )

    r.raise_for_status()

    out = r.json()["translations"][0]["text"]
    CACHE[k] = out

    return out


def translate_text(text, lang):

    if not isinstance(text, str) or not text.strip():
        return text

    return deepl_translate(text, lang)


def walk(obj, lang):

    if isinstance(obj, str):
        return translate_text(obj, lang)

    if isinstance(obj, dict):
        return {k: walk(v, lang) for k, v in obj.items()}

    if isinstance(obj, list):
        return [walk(i, lang) for i in obj]

    return obj


def translate_yaml(src, lang):

    data = yaml.safe_load(Path(src).read_text(encoding="utf-8"))
    out = walk(data, lang)
    dst = Path(src).parent / f"{lang}{Path(src).suffix}"

    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False)


def translate_json(src, lang):

    data = json.loads(Path(src).read_text(encoding="utf-8"))
    out = walk(data, lang)
    dst = Path(src).parent / f"{lang}.json"

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)


def translate_md(src, lang):

    text = Path(src).read_text(encoding="utf-8")
    out = translate_text(text, lang)
    dst = Path(src).with_name(f"{Path(src).stem}.{lang}.md")
    Path(dst).write_text(out, encoding="utf-8")


def process(file):

    for lang in TARGET_LANGS:

        if file.name in ("README.md", "DOCS.md"):
            translate_md(file, lang)

        elif file.name in ("de.yaml", "de.yml"):
            translate_yaml(file, lang)

        elif file.name == "de.json":
            translate_json(file, lang)


def main():

    input_file = Path(sys.argv[1])

    files = [
        Path(x.strip())
        for x in input_file.read_text().splitlines()
        if x.strip()
    ]

    for f in files:
        if f.exists():
            process(f)

    save_cache()


if __name__ == "__main__":
    main()
