# Plugins

Plugins ermöglichen die dynamische Ermittlung von Badge-Werten zur Laufzeit.

## Erstellen eines Plugins

Lege eine Datei unter `.github/scripts/plugins/<name>.py` an:

```python
from plugins.base import BadgePlugin


class Plugin(BadgePlugin):

    def generate(self, app_data, definition):
        # app_data = {"app": config.yaml, "var": .var.yaml}
        # definition = Badge-Definition aus config.yaml

        return {
            "value": "mein-wert",
            "color": "green"   # optional
        }
```

## Verwenden eines Plugins in config.yaml

```yaml
badges:
  mein_badge:
    type: plugin
    plugin: name_des_plugins   # entspricht plugins/<name>.py
    group: meta
    label: "Mein Badge"
```

## Mitgelieferte Plugins

| Plugin | Beschreibung |
|--------|-------------|
| `github_release` | Gibt die App-Version aus config.yaml zurück |
| `docker` | Docker-Image-Info (Stub) |
| `custom` | Generischer Custom-Badge |

## Beispiel: GitHub-Release-Version

```yaml
badges:
  upstream_release:
    type: plugin
    plugin: github_release
    group: upstream
    label: Release
```
