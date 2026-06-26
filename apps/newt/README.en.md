### Home Assistant Add-On:
## Newt Client for Pangolin Reverse Proxy Tunnels

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

Newt is a Home Assistant add-on for the Pangolin WireGuard tunnel client and TCP/UDP proxy. It securely connects your Home Assistant host to a Pangolin server and enables access to private services via a user-space WireGuard tunnel.

## Overview

- Add-on for the Pangolin Newt client
- Uses `host_network` for direct host network access
- Requires additional permissions: `NET_ADMIN`, `SYS_MODULE`
- Supported architectures: `aarch64`, `amd64`

## Installation

[![Open your Home Assistant instance and display the "Add App" repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev)

1. Open Home Assistant.
2. Go to **Settings → Add-ons → Add-on Store → ⋮ → Repositories**.
3. Add the repository: `https://github.com/sandmaennchen5/ha-repo-dev`
4. Install the **Newt** add-on.
5. Configure the add-on options.
6. Start the add-on.

> Enable Docker socket access: Disable **Protection Mode** on the add-on’s main page.

## Add-on Configuration

| Option | Type | Description |
|--------|-----|--------------|
| `endpoint` | `str` | URL of the Pangolin server, e.g., `https://app.pangolin.net` |
| `id` | `str` | Newt ID from the Pangolin dashboard |
| `secret` | `str` | Newt secret from the Pangolin dashboard |
| `extras.log_level` | `str` | `trace`, `debug`, `info`, `warn`, `error` (default: `info`) |

## Where can I find `id` and `secret`?

1. Open the Pangolin dashboard.
2. Select the desired site or create a new one.
3. Copy the generated `id` and `secret` from the site credentials.

## Prerequisites

- A running Pangolin server or a managed Pangolin instance
- A site registered in Pangolin with a Newt ID and secret

## Notes

- The add-on uses `host_network` so that the tunnel can be operated directly over the host network.
- The add-on must be restarted after making changes to the configuration.

## Additional Documentation

- See [DOCS.md](DOCS.md) for complete add-on documentation and troubleshooting.
- See [CHANGELOG.md](CHANGELOG.md) for the upstream release overview.

## Links

- [Pangolin Documentation](https://docs.pangolin.net)
- [Newt GitHub Repository](https://github.com/fosrl/newt)

[builder-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite
[builder-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=lintcode&label=Lint
[lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[docker-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
