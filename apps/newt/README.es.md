### Complemento de Home Assistant:
## Newt Client para túneles de proxy inverso de Pangolin

[![Builder][builder-badge]][builder-url]
[![Lint][lint-badge]][lint-url]
[![Docker Lint][docker-lint-badge]][docker-lint-url]
[![Yaml Lint][yaml-lint-badge]][yaml-lint-url]

<!-- BADGES-START -->
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
<!-- BADGES-END -->

Newt es un complemento de Home Assistant para el cliente de túnel WireGuard y el proxy TCP/UDP de Pangolin. Conecta de forma segura tu host de Home Assistant con un servidor Pangolin y permite el acceso a servicios privados a través de un túnel WireGuard en el espacio de usuario.

## Resumen

- Complemento para el cliente Pangolin Newt
- Utiliza `host_network` para el acceso directo a la red del host
- Requiere permisos adicionales: `NET_ADMIN`, `SYS_MODULE`
- Arquitecturas compatibles: `aarch64`, `amd64`

## Instalación

[![Abre tu instancia de Home Assistant y muestra el cuadro de diálogo para añadir un repositorio de aplicaciones con una URL de repositorio específica ya rellenada.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsandmaennchen5%2Fha-repo-dev)

1. Abre Home Assistant.
2. Ve a **Configuración → Complementos → Tienda de complementos → ⋮ → Repositorios**.
3. Añade el repositorio: `https://github.com/sandmaennchen5/ha-repo-dev`
4. Instala el complemento **Newt**.
5. Configura las opciones del complemento.
6. Inicia el complemento.

> Activa el acceso al socket de Docker: desactiva el **modo de protección** en la página principal del complemento.

## Configuración del complemento

| Opción | Tipo | Descripción |
|--------|-----|--------------|
| `endpoint` | `str` | URL del servidor de Pangolin, p. ej., `https://app.pangolin.net` |
| `id` | `str` | ID de Newt del panel de control de Pangolin |
| `secret` | `str` | Secreto de Newt del panel de control de Pangolin |
| `extras.log_level` | `str` | `trace`, `debug`, `info`, `warn`, `error` (por defecto: `info`) |

## ¿Dónde puedo encontrar el `id` y el `secret`?

1. Abre el panel de control de Pangolin.
2. Selecciona el sitio que desees o crea uno nuevo.
3. Copia el `id` y el `secret` generados de los datos de acceso del sitio.

## Requisitos previos

- Un servidor Pangolin en funcionamiento o una instancia gestionada de Pangolin
- Un sitio registrado en Pangolin con un Newt-ID y un secreto

## Notas

- El complemento utiliza `host_network` para que el túnel pueda funcionar directamente a través de la red del host.
- Tras realizar cambios en la configuración, es necesario reiniciar el complemento.

## Documentación adicional

- Consulta [DOCS.md](DOCS.md) para obtener la documentación completa del complemento y la guía de resolución de problemas.
- Consulta [CHANGELOG.md](CHANGELOG.md) para ver el resumen de versiones del proyecto original.

## Enlaces

- [Documentación de Pangolin](https://docs.pangolin.net)
- [Repositorio de Newt en GitHub](https://github.com/fosrl/newt)

[builder-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/hasos_app.yml?logo=buildkite
[builder-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/hasos_app.yml
[lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=lintcode&label=Lint
[lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
[docker-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/docker-lint.yaml?logo=Docker&label=DockerLint
[docker-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/docker-lint.yaml
[yaml-lint-badge]: https://img.shields.io/github/actions/workflow/status/sandmaennchen5/ha-repo-dev/yaml-lint.yaml?logo=yaml&label=YamlLint
[yaml-lint-url]: https://github.com/sandmaennchen5/ha-repo-dev/actions/workflows/yaml-lint.yaml
