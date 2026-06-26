# Badge-Konfiguration

Badges werden in `.github/config.yaml` im ersten YAML-Abschnitt (vor `---`) konfiguriert.

## Struktur

```yaml
defaults:
  color: blue
  style: flat-square
  separator: ', '
  shields:
    preset_name: https://img.shields.io/badge/label-{value}-blue

groups:
  group_id:
    order: 10
    title: Gruppenname

badges:
  badge_id:
    type: field          # field | bool | list | text | plugin
    group: runtime
    label: "Label"
    source: config.field  # oder var.field
    shield: https://img.shields.io/badge/...{value}...
    show_empty: false
    transforms:
      - type: replace
        from: "-"
        to: "--"
```

## Badge-Typen

| Typ | Beschreibung |
|-----|-------------|
| `field` | Einzelner Wert aus config.yaml oder .var.yaml |
| `bool` | true/false mit konfigurierbaren Farben |
| `list` | Liste von Werten, verbunden mit Separator |
| `text` | Statischer Text |
| `plugin` | Wert aus einem Python-Plugin |

## Transforms

Transforms werden sequenziell auf den Wert angewendet:

| Typ | Parameter | Beschreibung |
|-----|-----------|-------------|
| `replace` | `from`, `to` | Zeichen ersetzen |
| `join` | `separator` | Liste → String |
| `split` | `separator` | String → Liste |
| `lower` | – | Kleinbuchstaben |
| `upper` | – | Großbuchstaben |
| `title` | – | Title Case |
| `trim` | – | Whitespace entfernen |
| `url_encode` | – | URL-Encoding |
| `regex_replace` | `pattern`, `replacement` | Regex-Ersetzung |
| `prefix` | `value` | Präfix hinzufügen |
| `suffix` | `value` | Suffix hinzufügen |
| `default` | `value` | Standardwert wenn leer |
| `sort` | – | Liste sortieren |
| `unique` | – | Duplikate entfernen |

## shields.io Optionen

Alle badges unterstützen:
- `logo`: SimpleIcons Name (https://simpleicons.org/)
- `logoColor`: Farbe des Logos
- `logoUrl`: Manuelle Logo-URL
- `style`: `flat`, `flat-square`, `plastic`, `for-the-badge`, `social`
- `color`: Farbe des Wert-Teils
- `query`: Zusätzliche Query-Parameter

## App-spezifische Overrides (.var.yaml)

```yaml
badge_overrides:
  version:
    color: red
    prefix: "v"

group_overrides:
  runtime:
    style: for-the-badge

hide_badges:
  - python_version

hide_groups:
  - upstream
```
