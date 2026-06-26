# Translation Workflow

## Overview

Automatic translation workflow for maintaining multiple language versions of documentation and configuration files.

## Branch Structure

### `i18n-update`
- **Purpose**: Contains translated files (README.en.md, de.yaml, fr.json, etc.)
- **Audience**: Pull requests to main, meant for code review
- **Contents**: ONLY translated output files
- **Cache**: NOT included (see i18n-cache branch)

### `i18n-cache`
- **Purpose**: Stores translation cache for performance
- **Audience**: Internal use only, not reviewed
- **Contents**: `.i18n_cache/` directory with translation_cache.json
- **Auto-synced**: Updated automatically after each translation run

### Workflow (Main)
- Trigger: Push to main with changes to German source files (de.yaml, de.json, de.md)
- Action: Automatically creates/updates translations on i18n-update and caches on i18n-cache

## Working Locally

### Setup

```bash
# Fetch translation branches
git fetch origin i18n-update i18n-cache

# Create temporary working branch
git checkout -b feature/translate-docs origin/main
```

### Running Translations Locally

```bash
# Install dependencies
pip install requests pyyaml

# Get files changed vs main
git diff --name-only origin/main...HEAD > changed_files.txt

# Run translator
TARGET_LANGUAGES=en,fr,de python .github/scripts/translate.py changed_files.txt
```

### Testing Translations

```bash
# Check generated files
find . -type f -name "*.en.md" -o -name "*.fr.yaml"

# Verify cache was created
cat .i18n_cache/translation_cache.json | jq 'length'

# View cached translations
cat .i18n_cache/translation_cache.json | jq '.' | head -50
```

## Files

- `.github/workflows/translate.yml` - Main workflow definition
- `.github/scripts/translate.py` - Translation script
- `.i18n_cache/` - Local cache (in .gitignore, never committed to i18n-update)
  - `translation_cache.json` - Cache of translated strings
  - `changed_files.json` - Track of changed files

## Configuration

Set in GitHub Actions Variables:
- `TARGET_LANGUAGES`: Comma-separated list (e.g., "en,fr,es,de")

Set in GitHub Actions Secrets:
- `DEEPL_API_KEY`: Optional, uses free MyMemory API as fallback

## How It Works

1. **Change Detection**: Detect changes to German source files
2. **Cache Restore**: Load previous translation cache from i18n-cache branch
3. **Translate**: Use DeepL API (or free fallback) to translate changed files
4. **Split Commit**: 
   - Translations → i18n-update branch (for PR)
   - Cache → i18n-cache branch (for next run)
5. **PR Management**: Update or create pull request on i18n-update

## Performance Notes

- First run: Creates new translations and cache
- Subsequent runs: Uses cache to avoid re-translating unchanged strings
- Cache persists across workflow runs via i18n-cache branch
- Free MyMemory API used as fallback when DeepL is not available

## Troubleshooting

**No translations generated:**
- Check that files match patterns: `de.yaml`, `de.json`, `README.md`, `DOCS.md`
- Verify `TARGET_LANGUAGES` environment variable is set

**Cache not found:**
- i18n-cache branch may not exist yet, will be created on first run

**Translation quality issues:**
- Check logs for API errors
- Consider adding DeepL API key for better translations

## Manual Cache Management

To reset cache:
```bash
# Delete cache on i18n-cache branch
git checkout i18n-cache
rm -rf .i18n_cache
git add .
git commit -m "chore: reset translation cache"
git push origin i18n-cache
```
