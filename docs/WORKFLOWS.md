# Workflows

## hasos_app.yml – App Builder

**Trigger:** Push/PR auf `main` (wenn App-Dateien geändert), oder manuell per `workflow_dispatch`.

**Funktion:**
- Erkennt geänderte Apps automatisch
- Baut Docker-Images für alle unterstützten Architekturen
- Veröffentlicht beim Push auf `main`
- Manueller Trigger ermöglicht Auswahl einer einzelnen App

**Reusable Workflow:** `build-app.yaml` wird von `hasos_app.yml` aufgerufen.

---

## update_readme.yml – README Badge-Generator

**Trigger:** Push auf `main` wenn App-Configs oder Badge-Konfiguration geändert.

**Funktion:**
- Generiert Badges aus App-Metadaten
- Aktualisiert `<!-- BADGES-START -->..<!-- BADGES-END -->` Marker in READMEs
- Committet Änderungen automatisch

---

## generate_dashboard.yml – Dashboard-Generator

**Trigger:** Nach `update_readme.yml` oder wenn Dashboard-Dateien geändert.

**Funktion:**
- Erstellt History-Snapshot
- Exportiert Health-Daten
- Generiert HTML-Dashboard
- Publiziert auf `dashboard`-Branch (GitHub Pages)

---

## badge-lint.yml – Badge & Schema Validation

**Trigger:** PR, Push auf `main`, manuell.

**Funktion:**
- Validiert `.github/config.yaml` gegen JSON-Schema
- Validiert `apps/**/config.yaml` und `.var.yaml`
- Führt Health-Check aus

---

## yaml-lint.yaml – YAML Lint

**Trigger:** Push, täglich um 04:00 Uhr.

---

## docker-lint.yaml – Dockerfile Lint

**Trigger:** Push wenn Dockerfiles geändert, täglich um 04:00 Uhr.

---

## translate.yml – Übersetzungen

**Trigger:** Push wenn deutsche Dokumentation geändert.

**Funktion:**
- Übersetzt README.md, DOCS.md und translations/de.yaml via DeepL
- Erstellt PR mit den Übersetzungen

**Voraussetzungen:** Secret `DEEPL_API_KEY` und Variable `TRANSLATION_LANGUAGES`.

---

## update-workflow-options.yaml – App-Dropdown aktualisieren

**Trigger:** Push wenn neue App-Config hinzugefügt, manuell.

**Funktion:**
- Aktualisiert die App-Auswahl im `hasos_app.yml` Workflow-Dropdown
