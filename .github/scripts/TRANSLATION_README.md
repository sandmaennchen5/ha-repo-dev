# Automatic Translation System

Dieses System übersetzt automatisch deutsche Dateien (README, DOCS, Translationen) in mehrere Sprachen.

## Funktionsweise

### Workflow-Trigger

Der Workflow wird automatisch ausgelöst, wenn:
- Deutsche Dateien auf `main` gepusht werden
- Manuelle Ausführung über `workflow_dispatch` erfolgt

### Unterstützte Dateien

- `README.md` und `DOCS.md` (Root)
- `apps/*/README.md` und `apps/*/DOCS.md`
- `apps/*/translations/de.yaml|yml|json`

### Übersetzungsprozess

1. **Branch-Management**: Der `i18n-update` Branch wird erstellt oder aktualisiert
2. **Datei-Erkennung**: Nur geänderte deutsche Dateien werden verarbeitet
3. **Übersetzung**: 
   - Primär: DeepL API (mit `DEEPL_API_KEY`)
   - Fallback: MyMemory Free Translation API (kostenlos, ohne Key)
4. **Caching**: Übersetzungen werden gecacht, um API-Zugriffe zu minimieren
5. **PR-Verwaltung**: Automatische PR-Erstellung und Aktualisierung

## Konfiguration

### GitHub Secrets

```
DEEPL_API_KEY          # Optional: DeepL Pro/Free API Key
```

### GitHub Variables

```
TARGET_LANGUAGES       # Zielsprachen (Komma-getrennt)
                      # Standard: "en"
                      # Beispiel: "en,fr,es,it"
```

### Unterstützte Sprachen

- `en` - English
- `fr` - Français
- `es` - Español
- `it` - Italiano
- `pt` - Português
- `nl` - Nederlands
- `pl` - Polski
- `ru` - Русский
- `ja` - 日本語
- `zh` - 中文

## Cache-System

Die `.i18n_cache/` Verzeichnis enthält:

- `translation_cache.json`: Gecachte Übersetzungen (Key-Hash → Übersetzung)
- `changed_files.json`: Protokoll geänderter Dateien

Der Cache liegt im `i18n-update` Branch und wird zwischen Ausführungen wiederverwendet, um API-Kosten zu sparen.

## Output-Dateien

Generierte Übersetzungen:

```
README.md           → README.en.md, README.fr.md, ...
DOCS.md             → DOCS.en.md, DOCS.fr.md, ...
translations/de.yaml → translations/en.yaml, translations/fr.yaml, ...
```

## Workflow-Schritte

### 1. Vorbereitung
- Main Branch auschecken
- i18n-update Branch erstellen/aktualisieren
- Auf Main rebasen

### 2. Datei-Analyse
- Geänderte deutsche Dateien ermitteln
- Cache von i18n-update laden

### 3. Übersetzung
- Jede Datei in Zielsprachen übersetzen
- Nur neue/geänderte Dateien verarbeiten
- Cache nach jeder Übersetzung speichern

### 4. Commit & Push
- Übersetzungen committen
- i18n-update pushen
- Cache speichern

### 5. PR-Management
- Neue PR erstellen (wenn nicht existiert)
- Existierende PR aktualisieren
- Labels und Kommentare hinzufügen

## Fehlerbehandlung

### DeepL nicht verfügbar
- Fallback auf MyMemory API (kostenlos)
- Warnung im Workflow-Log

### Rate-Limiting
- Cache verhindert doppelte Anfragen
- Fallback schützt vor API-Limits

### Merge-Konflikte
- Rebase-Fehler bricht Workflow ab
- Manuell in i18n-update branch beheben

## Best Practices

### German Source Files

Schreibe klare, strukturierte Deutsche Texte:

```markdown
# Überschrift

Hier der Text mit klaren Absätzen.

- Punkt 1
- Punkt 2
```

### YAML/JSON Dateien

Nutze konsistente Struktur:

```yaml
# de.yaml
app:
  title: "Meine App"
  description: "Beschreibung"
  features:
    - name: "Feature 1"
      desc: "Beschreibung"
```

### Git Workflow

Nur Deutsche Dateien ändern → Workflow übernimmt Übersetzung:

```bash
git add apps/myapp/README.md
git add apps/myapp/translations/de.yaml
git commit -m "docs: update german documentation"
git push origin main
# → Workflow startet automatisch
```

## Troubleshooting

### PR wird nicht erstellt

1. Check `GITHUB_TOKEN` Permissions
2. Verify `TARGET_LANGUAGES` Variable ist gesetzt
3. Prüfe GitHub Actions Logs

### Übersetzungen sind schlecht

- DeepL: Verbessere deutsche Quelle
- MyMemory: Zielsprache kann begrenzt sein
- Nutze `DEEPL_API_KEY` für bessere Qualität

### Cache wird nicht genutzt

1. `.i18n_cache/` muss in i18n-update Branch sein
2. Cache-Datei muss committet sein
3. Check `git log` in i18n-update Branch

### Nur manche Dateien übersetzt

- Prüfe Dateiname (muss `README.md`, `DOCS.md` oder `de.yaml` sein)
- Prüfe Dateipfad (muss Root oder `apps/*/` sein)
- Check GitHub Actions Logs für Details

## Manuelle Ausführung

Workflow manuell starten ohne Push:

```bash
gh workflow run translate.yml -r main
```

Oder via GitHub UI:
1. Actions Tab
2. "Automatic Translation"
3. "Run workflow" Button

## API Kosten

### DeepL

- Free Tier: 500.000 Zeichen/Monat
- Pro: Unlimited

### MyMemory

- Kostenlos: Unbegrenzt (mit Fair-Use Policy)
- Keine Authentifizierung notwendig

## Limits beachten

- Dateigröße: Keine hard Limits
- API Timeout: 30 Sekunden pro Request
- Concurrent Requests: 1 (sequenziell)

---

Konfiguriert unter: `.github/workflows/translate.yml`
Python Script: `.github/scripts/translate.py`
