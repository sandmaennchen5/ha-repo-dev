### 1Home Assistant Add-On: test2
## Newt Client für Pangolin-Reverse-Proxy-Tunnel

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![Yaml Lint][yaml-lint-badge]][yaml-lint-url]

<!-- BADGES-START -->
![Version](https://img.shields.io/badge/version-v1.13.0-blue)
![Updated](https://img.shields.io/badge/updated-2026--06--26-green)
![Stage](https://img.shields.io/badge/stage-stable-orange)
![Privileged](https://img.shields.io/badge/privileged-NET_ADMIN%7CSYS_MODULE-red)
![Arch](https://img.shields.io/badge/arch-aarch64%2C%20amd64-green)
![Host Network](https://img.shields.io/badge/host_network-True-blue)
![Docker API](https://img.shields.io/badge/docker_api-True-blue)
![Kernel Modules](https://img.shields.io/badge/kernel_modules-True-blue)
![Upstream](https://img.shields.io/badge/upstream-v1.13.0-yellow)
![Repo](https://img.shields.io/badge/repo-github.com%2Ffosrl%2Fnewt-informational)
<!-- BADGES-END -->

Newt ist ein Home Assistant Add-on für den Pangolin WireGuard-Tunnel-Client und TCP/UDP-Proxy. Es verbindet deinen Home Assistant Host sicher mit einem Pangolin-Server und ermöglicht Zugriff auf private Dienste über einen User-Space WireGuard-Tunnel.

## Übersicht

- Add-on für den Pangolin Newt-Client
- Nutzt `host_network` für direkten Host-Netzwerkzugriff
- Erfordert zusätzliche Berechtigungen: `NET_ADMIN`, `SYS_MODULE`
- Unterstützte Architekturen: `aarch64`, `amd64`

## Installation

[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev)

1. Öffne Home Assistant.
2. Gehe zu **Einstellungen → Add-ons → Add-on Store → ⋮ → Repositories**.
3. Füge das Repository hinzu: `https://github.com/sandmaennchen5/ha-repo-dev`
4. Installiere das Add-on **Newt**.
5. Konfiguriere die Add-on-Optionen.
6. Starte das Add-on.

> Aktiviere den Docker-Socket-Zugriff: **Schutzmodus** auf der Hauptseite des Add-ons deaktivieren.

## Add-on-Konfiguration

| Option | Typ | Beschreibung |
|--------|-----|--------------|
| `endpoint` | `str` | URL des Pangolin-Servers, z. B. `https://app.pangolin.net` |
| `id` | `str` | Newt-ID aus dem Pangolin-Dashboard |
| `secret` | `str` | Newt-Secret aus dem Pangolin-Dashboard |
| `extras.log_level` | `str` | `trace`, `debug`, `info`, `warn`, `error` (Standard: `info`) |

## Wo finde ich `id` und `secret`?

1. Öffne das Pangolin-Dashboard.
2. Wähle die gewünschte Site aus oder lege eine neue an.
3. Kopiere die generierte `id` und das `secret` aus den Site-Anmeldeinformationen.

## Voraussetzungen

- Ein laufender Pangolin-Server oder eine verwaltete Pangolin-Instanz
- Eine in Pangolin registrierte Site mit Newt-ID und Secret

## Hinweise

- Das Add-on nutzt `host_network`, damit der Tunnel direkt über das Host-Netzwerk betrieben werden kann.
- Nach Änderungen an der Konfiguration muss das Add-on neu gestartet werden.

## Weitere Dokumentation

- Siehe [DOCS.md](DOCS.md) für vollständige Add-on-Dokumentation und Troubleshooting.
- Siehe [CHANGELOG.md](CHANGELOG.md) für den upstream Release-Überblick.

## Links

- [Pangolin Dokumentation](https://docs.pangolin.net)
- [Newt GitHub Repository](https://github.com/fosrl/newt)

[builder-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite
[builder-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=lintcode&label=Lint
[lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[docker-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
