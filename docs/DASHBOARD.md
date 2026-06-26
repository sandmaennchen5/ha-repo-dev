# Dashboard

Das Dashboard wird automatisch durch den Workflow `generate_dashboard.yml` generiert und auf dem `dashboard`-Branch als GitHub Pages veröffentlicht.

## Konfiguration

Der Dashboard-Abschnitt in `.github/config.yaml` (nach dem ersten `---`):

```yaml
site:
  title: "HassOS Apps Dashboard"
  subtitle: "Home Assistant Apps & Add-ons"
  branch: dashboard
  base_url: "/ha-repo-dev"
  asset_path: assets
  footer: "Generated automatically"

theme:
  cards: true
  rounded: true
  show_icons: true

navigation:
  enabled: true
  items:
    - title: Dashboard
      icon: 📊
      url: /
```

## Seiten

| Seite | URL | Beschreibung |
|-------|-----|-------------|
| Index | `/` | Übersicht mit Health-Score-Karten |
| Apps | `/apps/` | Liste aller Apps mit Badges |
| App | `/apps/<slug>/` | Detailseite einer App |
| Matrix | `/matrix.html` | Badge-Matrix aller Apps |
| Health | `/health.html` | Health-Checks und Warnungen |
| History | `/history.html` | Badge-Score-Verlauf |
| Badge Lab | `/lab.html` | Badge-Vorschau und Test |
| Settings | `/settings.html` | Dashboard-Einstellungen |

## Generierung

```bash
# Lokal ausführen:
cd .github/scripts
python dashboard/history_generator.py
python dashboard/health_export.py
python dashboard/dashboard_generator.py
```

Das Dashboard wird dann im Ordner `.dashboard/` erstellt.

## History

Der Score-Verlauf wird im Branch `main` unter `.history/history.json` gespeichert und enthält bis zu 365 Einträge.
