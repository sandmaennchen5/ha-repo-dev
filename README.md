# HassOS Apps Repository – sandmaennchen5

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![YAML Lint][yaml-lint-badge]][yaml-lint-url]

Home  Assistant App-Repository mit vollautomatischer Badge- und Dashboard-Generierung.

## Installation

[![Repository hinzufügen][repoadd-badge]][repoadd]

### Manuell

1. Öffne Home Assistant.
2. **Einstellungen → Add-ons → Add-on Store → ⋮ → Repositories**
3. URL hinzufügen:
   ```
   https://github.com/sandmaennchen5/ha-repo-dev
   ```
4. Klicke auf **Hinzufügen** und aktualisiere den Store.

## Apps

<!-- APPS-LIST-START -->
## [🛰️ Newt - Pangolin Tunnels](apps/newt/)

Secure remote access with Pangolin tunnels.

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

<!-- APPS-LIST-END -->

## Dashboard

Das automatisch generierte Dashboard mit Badge-Matrix, Health-Score und History ist verfügbar auf:
**[GitHub Pages Dashboard](https://sandmaennchen5.github.io/ha-repo-dev/)**

## Unterstütze die Entwicklung

[![PayPal][paypal-badge]][paypal-link]

## Support

- [Home Assistant Community Forum][forum]
- [Issues in diesem Repository](https://github.com/sandmaennchen5/ha-repo-dev/issues)

---

[builder-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite&label=Builder
[builder-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/badge-lint.yml?logo=lintcode&label=Lint
[lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/badge-lint.yml
[docker-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[repoadd-badge]: https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg
[repoadd]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev
[paypal-badge]: https://img.shields.io/badge/PayPal-Spenden-blue?logo=paypal
[paypal-link]: https://www.paypal.me/sandmaennchen5
[forum]: https://community.home-assistant.io/
