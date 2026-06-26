### Extension Home Assistant :
## Newt Client pour les tunnels de proxy inverse Pangolin

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![Yaml Lint][yaml-lint-badge]][yaml-lint-url]

<!-- BADGES-START -->
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
<!-- BADGES-END -->

Newt est un add-on Home Assistant pour le client de tunnel WireGuard Pangolin et le proxy TCP/UDP. Il connecte votre hôte Home Assistant de manière sécurisée à un serveur Pangolin et permet d’accéder à des services privés via un tunnel WireGuard en espace utilisateur.

## Présentation

- Extension pour le client Pangolin Newt
- Utilise `host_network` pour un accès direct au réseau de l’hôte
- Nécessite des autorisations supplémentaires : `NET_ADMIN`, `SYS_MODULE`
- Architectures prises en charge : `aarch64`, `amd64`

## Installation

[![Ouvrez votre instance Home Assistant et affichez la boîte de dialogue d'ajout d'un référentiel d'applications avec une URL de référentiel spécifique préremplie.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev)

1. Ouvre Home Assistant.
2. Rends-toi dans **Paramètres → Extensions → Boutique d’extensions → ⋮ → Référentiels**.
3. Ajoute le référentiel : `https://github.com/sandmaennchen5/ha-repo-dev`
4. Installe l’extension **Newt**.
5. Configure les options de l’extension.
6. Lancez l’add-on.

> Activez l’accès au socket Docker : désactivez le **mode de protection** sur la page principale de l’add-on.

## Configuration de l’add-on

| Option | Type | Description |
|--------|-----|--------------|
| `endpoint` | `str` | URL du serveur Pangolin, par exemple `https://app.pangolin.net` |
| `id` | `str` | ID Newt issu du tableau de bord Pangolin |
| `secret` | `str` | Clé secrète Newt issue du tableau de bord Pangolin |
| `extras.log_level` | `str` | `trace`, `debug`, `info`, `warn`, `error` (par défaut : `info`) |

## Où trouver `id` et `secret` ?

1. Ouvrez le tableau de bord Pangolin.
2. Sélectionnez le site souhaité ou créez-en un nouveau.
3. Copiez l’`id` et le `secret` générés à partir des informations d’identification du site.

## Prérequis

- Un serveur Pangolin en cours d’exécution ou une instance Pangolin gérée
- Un site enregistré dans Pangolin avec un Newt-ID et un secret

## Remarques

- L’extension utilise `host_network` afin que le tunnel puisse fonctionner directement via le réseau hôte.
- Après toute modification de la configuration, l’extension doit être redémarrée.

## Documentation complémentaire

- Consultez [DOCS.md](DOCS.md) pour la documentation complète de l’extension et le dépannage.
- Consultez [CHANGELOG.md](CHANGELOG.md) pour l’aperçu des versions en amont.

## Liens

- [Documentation Pangolin](https://docs.pangolin.net)
- [Dépôt GitHub de Newt](https://github.com/fosrl/newt)

[builder-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite
[builder-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=lintcode&label=Lint
[lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[docker-lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge] : https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url] : https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
