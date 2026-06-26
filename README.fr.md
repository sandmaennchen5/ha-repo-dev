# Référentiel d'applications HassOS – sandmaennchen5

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![YAML Lint][yaml-lint-badge]][yaml-lint-url]

Référentiel d'applications Home Assistant avec génération entièrement automatique de badges et de tableaux de bord.

## Installation

[![Ajouter un référentiel][repoadd-badge]][repoadd]

### Manuellement

1. Ouvrez Home Assistant.,
2. **Paramètres → Extensions → Boutique d'extensions → ⋮ → Référentiels**
3. Ajoute l'URL :
   ```
   https://github.com/sandmaennchen5/ha-repo-dev
   ```
4. Clique sur **Ajouter** et actualise la boutique.

## Applications

<!-- APPS-LIST-START -->
## [🛰️ Newt - Pangolin Tunnels](apps/newt/)

Accès distant sécurisé grâce aux tunnels Pangolin.

![Version](https://img.shields.io/badge/version-v1.13.0-blue)
![Mise à jour](https://img.shields.io/badge/updated-2026--06--26-green)
![Stage](https://img.shields.io/badge/stage-stable-orange)
![Privilégié](https://img.shields.io/badge/privileged-NET_ADMIN%7CSYS_MODULE-red)
![Arch](https://img.shields.io/badge/arch-aarch64%2C%20amd64-green)
![Réseau hôte](https://img.shields.io/badge/host_network-True-blue)
![API Docker](https://img.shields.io/badge/docker_api-True-blue)
![Modules du noyau](https://img.shields.io/badge/kernel_modules-True-blue)
![Upstream](https://img.shields.io/badge/upstream-v1.13.0-yellow)
![Repo](https://img.shields.io/badge/repo-github.com%2Ffosrl%2Fnewt-informational)

<!-- APPS-LIST-END -->

## Tableau de bord

Le tableau de bord généré automatiquement, avec la matrice des badges, le score de santé et l'historique, est disponible sur :
**[Tableau de bord GitHub Pages](https://sandmaennchen5.github.io/ha-repo-dev/)**

## Soutenez le développement

[![PayPal][paypal-badge]][paypal-link]

## Assistance

- [Forum de la communauté Home Assistant][forum]
- [Problèmes dans ce dépôt](https://github.com/sandmaennchen5/ha-repo-dev/issues)

---

[builder-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite&label=Builder
[builder-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/badge-lint.yml?logo=lintcode&label=Lint
[lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/badge-lint.yml
[docker-lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[repoadd-badge] : https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg
[repoadd] : https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev
[paypal-badge]: https://img.shields.io/badge/PayPal-Spenden-blue?logo=paypal
[paypal-link]: https://www.paypal.me/sandmaennchen5
[forum]: https://community.home-assistant.io/
