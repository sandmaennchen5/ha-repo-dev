# Troubleshooting

## Badges werden nicht aktualisiert

1. Prüfe ob die `<!-- BADGES-START -->` und `<!-- BADGES-END -->` Marker in der README.md vorhanden sind.
2. Führe den `Update README Badges` Workflow manuell aus.
3. Prüfe die GitHub Actions Logs.

```bash
# Lokal testen:
cd .github/scripts
pip install pyyaml
python readme_generator.py
```

## Schema-Validierungsfehler

```bash
cd .github/scripts
pip install pyyaml jsonschema
python schema_validator.py
```

Prüfe die Fehlerausgabe auf:
- Fehlende Pflichtfelder
- Ungültige Typen
- Unbekannte Felder

## Health-Check Warnungen

```bash
cd .github/scripts
python health_check.py
```

## Dashboard wird nicht generiert

1. Stelle sicher, dass der `update_readme.yml` Workflow erfolgreich war.
2. Führe `generate_dashboard.yml` manuell aus.
3. Prüfe ob GitHub Pages auf dem `dashboard`-Branch konfiguriert ist.

## App wird nicht gebaut

1. Prüfe ob die App einen gültigen `config.yaml` hat.
2. Prüfe ob `image` in `config.yaml` gesetzt ist.
3. Prüfe ob die Architektur in `arch` unterstützt wird.

## Übersetzungen funktionieren nicht

- Secret `DEEPL_API_KEY` muss gesetzt sein.
- Variable `TRANSLATION_LANGUAGES` (z.B. `en,fr`) muss gesetzt sein.
- Nur Dateien die `de.yaml`, `README.md` oder `DOCS.md` heißen werden übersetzt.
