# Konfiguration

## .github/config.yaml

Die zentrale Konfigurationsdatei ist in zwei Abschnitte aufgeteilt (getrennt durch `---`):

1. **Badge-Konfiguration** (defaults, groups, badges) – Abschnitt 1
2. **Dashboard-Konfiguration** (site, theme, navigation, …) – Abschnitt 2

## apps/<app>/config.yaml

Enthält alle Felder, die Home Assistant kennt:

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `name` | str | App-Name (Pflicht) |
| `version` | str | Version |
| `slug` | str | Eindeutiger Bezeichner |
| `description` | str | Kurzbeschreibung |
| `arch` | list | Unterstützte Architekturen |
| `image` | str | Docker-Image |
| `host_network` | bool | Host-Netzwerk |
| `docker_api` | bool | Docker-Socket Zugriff |
| `kernel_modules` | bool | Kernel-Module |
| `privileged` | list | Privilegierte Berechtigungen |
| `ingress` | bool | Ingress aktiviert |
| `startup` | str | `application`/`services`/`system` |
| `boot` | str | `auto`/`manual` |
| `watchdog` | str | Watchdog-URL |
| `options` | object | Standard-Konfigurationsoptionen |
| `schema` | object | Konfigurations-Schema |

## apps/<app>/.var.yaml

Enthält technische Metadaten, die HA nicht kennt:

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `hidden` | bool | App aus Root-README ausblenden |
| `icon` | str | Emoji vor dem App-Namen |
| `stage` | str | `stable`/`beta`/`lab` |
| `hide_root_readme` | bool | Nicht in Haupt-README anzeigen |
| `hide_app_readme` | bool | Badges in App-README nicht aktualisieren |
| `upstream_version` | str | Upstream-Version |
| `upstream_repo` | str | Upstream-Repository |
| `upstream_commit` | str | Upstream-Commit-Hash |
| `build` | str | Build-Status |
| `lint` | str | Lint-Status |
| `yaml_lint` | str | YAML-Lint-Status |
| `code_quality` | str | Code-Qualitäts-Score |
| `image_size` | str | Image-Größe |
| `custom_shield` | str | Komplette shields.io URL |
| `custom_flag` | str | Custom-Flag-Wert |
| `updated` | str | Datum der letzten Aktualisierung (YYYY-MM-DD) |
| `source` | str | Quell-Repository |
