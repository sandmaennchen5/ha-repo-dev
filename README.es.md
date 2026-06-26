# Repositorio de aplicaciones de HassOS – sandmaennchen5

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![YAML Lint][yaml-lint-badge]][yaml-lint-url]

Repositorio de aplicaciones de Home Assistant con generación totalmente automática de insignias y paneles de control.

## Instalación

[![Añadir repositorio][repoadd-badge]][repoadd]

### Manualmente

1. Abre Home Assistant.
2. **Configuración → Complementos → Tienda de complementos → ⋮ → Repositorios**
3. Añade la URL:
   ```
   https://github.com/sandmaennchen5/ha-repo-dev
   ```
4. Haz clic en **Añadir** y actualiza la tienda.

## Aplicaciones

<!-- APPS-LIST-START -->
## [🛰️ Newt - Pangolin Tunnels](apps/newt/)

Acceso remoto seguro con los túneles de Pangolin.

![Versión](https://img.shields.io/badge/version-v1.13.0-blue)
![Actualizado](https://img.shields.io/badge/updated-2026--06--26-green)
![Etapa](https://img.shields.io/badge/stage-stable-orange)
![Privilegiado](https://img.shields.io/badge/privileged-NET_ADMIN%7CSYS_MODULE-red)
![Arch](https://img.shields.io/badge/arch-aarch64%2C%20amd64-green)
![Red del host](https://img.shields.io/badge/host_network-True-blue)
![API de Docker](https://img.shields.io/badge/docker_api-True-blue)
![Módulos del kernel](https://img.shields.io/badge/kernel_modules-True-blue)
![Upstream](https://img.shields.io/badge/upstream-v1.13.0-yellow)
![Repositorio](https://img.shields.io/badge/repo-github.com%2Ffosrl%2Fnewt-informational)

<!-- APPS-LIST-END -->

## Panel de control

El panel de control generado automáticamente, con la matriz de insignias, la puntuación de estado y el historial, está disponible en:
**[Panel de control de GitHub Pages](https://sandmaennchen5.github.io/ha-repo-dev/)**

## Apoya el desarrollo

[![PayPal][paypal-badge]][paypal-link]

## Asistencia

- [Foro de la comunidad de Home Assistant][forum]
- [Incidencias en este repositorio](https://github.com/sandmaennchen5/ha-repo-dev/issues)

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
