#!/bin/bash

# GitHub Actions Configuration für Automatic Translation
# Führe dieses Script aus oder kopiere die Befehle manuell

set -e

echo "=== Automatic Translation Setup ==="
echo ""
echo "Dieses Script hilft beim Setup der Translation Workflow."
echo ""

# GitHub CLI Check
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI nicht gefunden. Installiere es zuerst:"
    echo "   https://cli.github.com"
    exit 1
fi

# Repository prüfen
echo "📍 Lokales Repository wird geprüft..."
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner')
if [ -z "$REPO" ]; then
    echo "❌ Kein GitHub Repository gefunden"
    exit 1
fi

echo "✓ Repository: $REPO"
echo ""

# Step 1: Variable setzen
echo "📝 GitHub Variables werden konfiguriert..."

# TARGET_LANGUAGES
read -p "Zielsprachen (Standard: en): " -e -i "en" TARGET_LANGS
echo "Setting TARGET_LANGUAGES = $TARGET_LANGS"
gh variable set TARGET_LANGUAGES --body "$TARGET_LANGS" || echo "⚠️  Variable konnte nicht gesetzt werden. Manuell prüfen."

echo "✓ TARGET_LANGUAGES = $TARGET_LANGS"
echo ""

# Step 2: Optional Secret für DeepL
echo "🔐 DeepL API Key (Optional)..."
read -p "Hast du einen DeepL API Key? (y/n): " -e -i "n" HAS_DEEPL

if [[ "$HAS_DEEPL" =~ ^[Yy]$ ]]; then
    read -sp "DeepL API Key eingeben: " DEEPL_KEY
    echo ""
    gh secret set DEEPL_API_KEY --body "$DEEPL_KEY" || echo "⚠️  Secret konnte nicht gesetzt werden."
    echo "✓ DEEPL_API_KEY gespeichert"
    echo "  (Fallback: MyMemory wird trotzdem genutzt)"
else
    echo "⚠️  DeepL API Key nicht gesetzt"
    echo "  → Fallback: MyMemory Free API wird verwendet"
    echo "  → Qualität: Gut für die meisten Sprachen"
fi

echo ""

# Step 3: Workflow testen
echo "🧪 Workflow wird getestet..."
read -p "Workflow jetzt testen? (y/n): " -e -i "n" RUN_WORKFLOW

if [[ "$RUN_WORKFLOW" =~ ^[Yy]$ ]]; then
    echo "Starte Workflow: translate.yml"
    gh workflow run translate.yml -r main
    echo "✓ Workflow gestartet"
    echo "  → Prüfe: Actions Tab im Repository"
else
    echo "Workflow später starten:"
    echo "  $ gh workflow run translate.yml -r main"
fi

echo ""
echo "=== Setup abgeschlossen ==="
echo ""
echo "Nächste Schritte:"
echo "1. ✓ Variablen konfiguriert"
echo "2. Erstelle eine Änderung an einer DE-Datei:"
echo "   - README.md"
echo "   - DOCS.md"
echo "   - apps/*/README.md"
echo "   - apps/*/translations/de.yaml"
echo "3. Pushe zum main Branch"
echo "4. Workflow läuft automatisch"
echo "5. PR wird erstellt mit Übersetzungen"
echo ""
echo "Dokumentation: .github/scripts/TRANSLATION_README.md"
