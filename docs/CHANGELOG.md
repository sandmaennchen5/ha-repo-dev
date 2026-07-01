# Changelog – Badge Framework

Dieses Changelog dokumentiert Änderungen am Badge-Framework und der Repository-Infrastruktur (nicht an einzelnen Apps).

## [1.0.0] – 2026-06-26

### Neu
- Vollständige Repository-Struktur für Home Assistant Add-ons und HACS
- Zentrale Konfigurationsdatei `.github/config.yaml` (Badge + Dashboard in einer Datei)
- **Transform-Pipeline** für Badges: `replace`, `join`, `split`, `lower`, `upper`, `title`, `trim`, `url_encode`, `regex_replace`, `prefix`, `suffix`, `default`, `sort`, `unique`
- Plugin-System für dynamische Badge-Werte (`.github/scripts/plugins/`)
- Badge-Gruppen: runtime, ha, system, security, meta, upstream, custom
- Automatische README-Generierung via `update_readme.yml`
- Dashboard-Generierung mit GitHub Pages (`generate_dashboard.yml`)
- Dashboard-Seiten: Index, Apps, Matrix, Health, History, Badge Lab, Settings
- GitHub Actions Workflows: Builder, Linter, Docker-Lint, YAML-Lint, Translate
- Schema-Validierung für `config.yaml`, `.var.yaml` und Badge-Konfiguration
- Health-Check mit Warnungen und Fehlern
- HACS-Verzeichnisstruktur: `blueprints/`, `custom_components/`, `themes/`, `python_scripts/`
- Beispiel-App `apps/example/` als Blueprint
- Newt App `apps/newt/` (Pangolin Tunnel Client)
- Vollständige Dokumentation unter `docs/`

### Technische Details
- Python 3.13, PyYAML, Jinja2, jsonschema
- shields.io Badges mit vollständiger Unterstützung für Logo (SimpleIcons), Farbe, Style
- History-Tracking bis zu 365 Einträgen
- DeepL-Integration für automatische Übersetzungen (DE → EN + andere Sprachen)
