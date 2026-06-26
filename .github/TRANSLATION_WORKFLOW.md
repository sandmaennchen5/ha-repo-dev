# Translation Workflow

## Overview

Automatic translation of German source files to multiple languages. Clean separation between translations (for review) and cache (for performance).

## Branch Structure

| Branch | Content | Purpose |
|--------|---------|---------|
| **i18-update** | Translated files (*.en.md, *.fr.yaml, etc.) | Pull Request to main |
| **i18n-cache** | Translation cache (.i18n_cache/) | Performance optimization |
| **main** | German source files (de.yaml, README.md) | Source of truth |

## Triggers

### Automatic (Push to main)
```
Changes to:
- README.md, DOCS.md
- apps/**/README.md, apps/**/DOCS.md
- apps/**/translations/de.yaml, de.yml, de.json
- .github/scripts/translate.py
```

### Manual (workflow_dispatch)
- Go to: Actions → Translation → Run workflow
- Options:
  - **Translate ALL files**: Check to translate entire repo
  - Otherwise: Only changed files

## How It Works

```
1. DETECT → Changed files or manual trigger
2. LOAD   → Cache from i18n-cache branch
3. FETCH  → Updated translations via DeepL/MyMemory
4. SPLIT  → 
   - Translations → i18-update branch
   - Cache → i18n-cache branch
5. CREATE → PR from i18-update to main
```

## Local Development

### Setup
```bash
# Fetch branches
git fetch origin i18-update i18n-cache

# Create working branch
git checkout -b feature/my-docs origin/main
```

### Test Translations
```bash
# Install dependencies
pip install requests pyyaml

# Translate changed files
TARGET_LANGUAGES=en,fr python .github/scripts/translate.py --help

# Translate ALL files
TARGET_LANGUAGES=en,fr python .github/scripts/translate.py --all

# Check specific changed file
git diff --name-only origin/main...HEAD > /tmp/files.txt
TARGET_LANGUAGES=en,fr python .github/scripts/translate.py /tmp/files.txt
```

### Verify Output
```bash
# Find generated translations
find . -name "*.en.md" -o -name "*.fr.yaml" -o -name "*.en.json"

# Check cache size
jq 'length' .i18n_cache/translation_cache.json

# View sample translations
jq 'to_entries | .[0:3]' .i18n_cache/translation_cache.json
```

## Script Usage

```bash
# Translate all files (finds German source files automatically)
python .github/scripts/translate.py --all

# Translate only changed files (from file list)
python .github/scripts/translate.py path/to/changed_files.txt

# Show help
python .github/scripts/translate.py --help
```

## Configuration

**GitHub Actions Variables** (`Settings → Variables`):
```
TARGET_LANGUAGES = en,fr,es,it,pt,nl,pl,ru,ja,zh
```

**GitHub Actions Secrets** (`Settings → Secrets`):
```
DEEPL_API_KEY = your-deepl-key-here
```

**Without DEEPL_API_KEY:**
- Falls back to free MyMemory API (slower, rate limited)
- Still works, just slower

## Translation Files Supported

**Markdown:**
- `README.md` → `README.en.md`, `README.fr.md`, etc.
- `DOCS.md` → `DOCS.en.md`, `DOCS.fr.md`, etc.
- `README_*.md` → `README_*.en.md`, `README_*.fr.md`, etc.

**Config (structured):**
- `de.yaml` → `en.yaml`, `fr.yaml`, etc.
- `de.yml` → `en.yml`, `fr.yml`, etc.
- `de.json` → `en.json`, `fr.json`, etc.

## Cache Management

### View Cache
```bash
# Size
jq 'length' .i18n_cache/translation_cache.json

# All entries
jq '.' .i18n_cache/translation_cache.json

# Specific language
jq 'to_entries[] | select(.key | contains("|en"))' .i18n_cache/translation_cache.json
```

### Reset Cache
```bash
# Local reset
rm .i18n_cache/translation_cache.json

# Remote reset (i18n-cache branch)
git checkout i18n-cache
rm -rf .i18n_cache
git add -A
git commit -m "chore: reset translation cache"
git push origin i18n-cache
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **No translations generated** | Check files match patterns (de.yaml, README.md, etc.) and TARGET_LANGUAGES is set |
| **Cache not loading** | i18n-cache branch doesn't exist yet - will be created on first run |
| **Slow translations** | Add DEEPL_API_KEY for faster DeepL API (vs free fallback) |
| **API errors in logs** | Check DEEPL_API_KEY validity and MyMemory API status |
| **PR not created** | Check that translations were actually generated (not "No changes") |
| **Duplicate PR** | Only one PR exists per time; updates auto-merge to it |

## Example Workflow Runs

### First Run (All Languages)
```
✓ Loaded cache with 0 entries
🔍 Scanning all files...
📝 README.md
  ✓ README.md → README.en.md
  ✓ README.md → README.fr.md
✅ Done! Generated 2 translations
📦 Cache saved with 45 entries
✓ Pushed to i18-update
✓ Cache updated on i18n-cache
✓ Created new PR
```

### Subsequent Push (Changed Files Only)
```
✓ Loaded cache with 45 entries
📌 Push detected changes: de.yaml
📝 de.yaml
  ✓ de.yaml → en.yaml
  ✓ de.yaml → fr.yaml
✅ Done! Generated 2 translations
📦 Cache saved with 47 entries
✓ Pushed to i18-update
✓ Cache updated on i18n-cache
✓ PR #42 already exists (auto-updated)
```
