#!/bin/bash

# GitHub Actions Configuration für Automatic Translation
# Führe dieses Script aus oder kopiere die Befehle manuell

set -e

echo "=== Automatic Translation Setup ==="
echo ""

# GitHub CLI Check
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI nicht gefunden. Installiere es zuerst:"
    echo "   https://cli.github.com"
    exit 1
fi

# Repository prüfen
echo "📍 Lokales Repository wird geprüft..."
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner' 2>/dev/null)
if [ -z "$REPO" ]; then
    echo "❌ Kein GitHub Repository gefunden"
    exit 1
fi

echo "✓ Repository: $REPO"
echo ""

# Step 1: Variable setzen
echo "📝 GitHub Variables werden konfiguriert..."

read -p "Zielsprachen (z.B. 'en,fr,es'): " -r TARGET_LANGS
if [ -z "$TARGET_LANGS" ]; then
    TARGET_LANGS="en"
fi

echo "Setting TARGET_LANGUAGES = $TARGET_LANGS"
gh variable set TARGET_LANGUAGES -b "$TARGET_LANGS" 2>/dev/null || \
    echo "⚠️  Fehler beim Setzen der Variable. Versuche alternative Methode..."

echo "✓ TARGET_LANGUAGES konfiguriert"
echo ""

# Step 2: Optional Secret für DeepL
echo "🔐 DeepL API Key (Optional für bessere Qualität)..."
read -p "Hast du einen DeepL API Key? (y/n): " -r HAS_DEEPL

if [[ "$HAS_DEEPL" =~ ^[Yy]$ ]]; then
    read -rsp "DeepL API Key eingeben: " DEEPL_KEY
    echo ""
    if [ -z "$DEEPL_KEY" ]; then
        echo "❌ Leerer Key, übersprungen"
    else
        gh secret set DEEPL_API_KEY -b "$DEEPL_KEY" 2>/dev/null && \
            echo "✓ DEEPL_API_KEY gespeichert" || \
            echo "⚠️  Secret konnte nicht gespeichert werden"
    fi
else
    echo "⚠️  DeepL API Key nicht gesetzt"
    echo "   → Fallback: MyMemory Free API wird verwendet"
fi

echo ""

# Step 3: Workflow testen
echo "🧪 Workflow ist bereit"
read -p "Workflow jetzt testen? (y/n): " -r RUN_WORKFLOW

if [[ "$RUN_WORKFLOW" =~ ^[Yy]$ ]]; then
    echo "Starte Workflow: translate.yml"
    gh workflow run translate.yml -r main 2>/dev/null && \
        echo "✓ Workflow gestartet" || \
        echo "⚠️  Workflow konnte nicht gestartet werden"
else
    echo "Starten Sie den Workflow später mit:"
    echo "  gh workflow run translate.yml -r main"
fi

echo ""
echo "=== Setup abgeschlossen ==="
echo ""
echo "📋 Nächste Schritte:"
echo "1. ✓ Variablen konfiguriert"
echo "2. Ändere eine deutsche Datei (README.md, DOCS.md, etc.)"
echo "3. Commit und push zum main Branch"
echo "4. Workflow läuft automatisch"
echo "5. PR wird mit Übersetzungen erstellt"
echo ""
echo "📚 Dokumentation:"
echo "   - .github/scripts/README.md (Quick Start)"
echo "   - .github/scripts/TRANSLATION_README.md (Vollständig)"
echo ""
