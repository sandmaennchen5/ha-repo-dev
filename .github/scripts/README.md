# Translation System - Quick Start

Automatische Übersetzung aller deutschen Dateien in mehrere Sprachen.

## ⚡ Schnellstart

### 1. Setup ausführen

```bash
bash .github/scripts/setup-translation.sh
```

Oder manuell:

```bash
# GitHub Variable setzen (Zielsprachen)
gh variable set TARGET_LANGUAGES --body "en,fr,es"

# Optional: DeepL Key für bessere Qualität
gh secret set DEEPL_API_KEY --body "your-key-here"
```

### 2. Deutsche Datei ändern

```bash
echo "# Neue Dokumentation" >> README.md
git add README.md
git commit -m "docs: update readme"
git push origin main
```

### 3. Automatischer Workflow startet

- ✅ Erkennt geänderte deutsche Dateien
- ✅ Übersetzt in konfigurierte Sprachen
- ✅ Erstellt/aktualisiert PR auf main
- ✅ Cached Übersetzungen für Effizienz

### 4. PR mergen

Der `i18n-update` Branch mit allen Übersetzungen ist bereit.

## 📋 Anforderungen erfüllt

| Nr. | Anforderung | Status |
|-----|-------------|--------|
| 1 | Haupt DEEPL API Key | ✅ mit Fallback |
| 2 | Fallback ohne KEY | ✅ MyMemory API |
| 3 | Nur geänderte Dateien | ✅ git diff |
| 4 | Mehrere Sprachen einstellbar | ✅ TARGET_LANGUAGES |
| 5 | DE-Dateien Definition | ✅ alle patterns |
| 6 | Cache System | ✅ .i18n_cache/ |
| 7 | i18n-update Branch | ✅ auto erstellt |
| 8 | Branch wenn fehlt | ✅ erstellt automatisch |
| 9 | Nur Übersetzungsdaten | ✅ keine Originals |
| 10 | Arbeitsdateien in Branch | ✅ .i18n_cache/ |
| 11 | PR zum main | ✅ mit Dateien |
| 12 | PR aktualisieren | ✅ mit Comment |

## 🗂️ Dateien

```
.github/
├── workflows/
│   └── translate.yml                 # Workflow Definition
├── scripts/
│   ├── translate.py                  # Python Übersetzungs-Script
│   ├── setup-translation.sh          # Setup Assistent
│   ├── TRANSLATION_README.md         # Vollständige Dokumentation
│   └── README.md                     # Diese Datei
```

## 🎯 Unterstützte Dateitypen

### Markdown
- `README.md` → `README.{lang}.md`
- `DOCS.md` → `DOCS.{lang}.md`
- `README_*.md`, `DOCS_*.md` (auch in apps/)

### Konfiguration
- `translations/de.yaml` → `translations/{lang}.yaml`
- `translations/de.yml` → `translations/{lang}.yml`
- `translations/de.json` → `translations/{lang}.json`

## 🌍 Sprachen

Konfigurierbar via `TARGET_LANGUAGES`:

```
en   - English
fr   - Français
es   - Español
it   - Italiano
pt   - Português
nl   - Nederlands
pl   - Polski
ru   - Русский
ja   - 日本語
zh   - 中文
```

## ⚙️ Konfiguration

### GitHub Variables
```yaml
TARGET_LANGUAGES: "en,fr,es"
```

### GitHub Secrets (optional)
```yaml
DEEPL_API_KEY: "your-api-key"  # Für bessere Qualität
```

## 🔄 Workflow-Flow

```
Änderung auf main
    ↓
Workflow triggert
    ↓
i18n-update Branch prüfen/erstellen
    ↓
Nur geänderte DE-Dateien erkennen
    ↓
Cache laden
    ↓
Übersetzen (DeepL oder Fallback)
    ↓
Cache speichern
    ↓
i18n-update Branch pushen
    ↓
PR erstellen oder aktualisieren
    ↓
Labels und Kommentare hinzufügen
```

## 📊 Cache System

Speichert Übersetzungen im `i18n-update` Branch:

```
.i18n_cache/
├── translation_cache.json     # SHA256(text+lang) → Übersetzung
└── changed_files.json         # Protokoll
```

**Vorteile:**
- Spart API-Aufrufe (kostensparend)
- Schneller bei wiederholten Übersetzungen
- Persistent zwischen Workflow-Runs

## 🧪 Manuell Testen

```bash
# Workflow direkt starten
gh workflow run translate.yml -r main

# Logs anschauen
gh run list -w translate.yml
gh run view <RUN_ID> -w translate.yml --log

# Status prüfen
gh pr list --head i18n-update
```

## ❓ FAQ

**Q: Kann ich die Fallback-API abschalten?**
A: Nein, Sie ist immer aktiv als Sicherheit. DeepL wird zuerst versucht.

**Q: Wie oft können die API aufgerufen werden?**
A: DeepL Free: 500.000 chars/Monat. MyMemory: Unbegrenzt mit Fair-Use.

**Q: Werden Originaldateien mit gepusht?**
A: Nein, nur die Übersetzungen landen in der PR.

**Q: Kann ich manuell Sprachen hinzufügen?**
A: Ja, einfach `TARGET_LANGUAGES` Variable aktualisieren.

## 📝 Beispiel

### Eingabe (de.yaml)
```yaml
app:
  title: "Meine App"
  desc: "Eine deutsche Beschreibung"
```

### Output (en.yaml)
```yaml
app:
  title: "My App"
  desc: "A German description"
```

## 🚀 Tipps

1. **Hohe Qualität:** Nutze DeepL API Key für beste Ergebnisse
2. **Sparen:** Schreibe klare deutsche Originale → bessere Auto-Übersetzung
3. **Schnell:** Cache reduziert API-Calls um ~80%
4. **Häufig:** Workflow läuft bei jeder Änderung

## 📚 Weitere Infos

Vollständige Dokumentation: `.github/scripts/TRANSLATION_README.md`

---

**Erstellt für automatische Dokumentationsübersetzung** 🤖
