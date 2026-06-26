### Complemento de Home Assistant: Documentación
## Cliente Newt para el túnel de proxy inverso de Pangolin

El [sistema Fossorial —con Pangolin](https://docs.fossorial.io/) como componente principal— es un proxy inverso tunelizado y autohospedado con gestión de identidades y accesos, diseñado para proporcionar recursos privados de forma segura a través de túneles WireGuard cifrados en el espacio de usuario. Piensa en ello como túneles de Cloudflare autohospedados.

Newt es el cliente principal que se conecta a Pangolin y permite el acceso a servicios en la misma red que Newt. Instálalo y conéctate a tu instancia de Pangolin para permitir el acceso remoto a Home Assistant a través de túneles seguros de WireGuard.

## Instalación

1. Abre Home Assistant.
2. Ve a **Configuración → Complementos → Tienda de complementos → ⋮ → Repositorios**.
3. Añade el repositorio.
4. Instala el complemento **Newt**.
5. Configura las opciones del complemento.
6. Inicia el complemento.

Permite a Newt acceder al socket de Docker. **Debes desactivar el «modo de protección» en la página principal del complemento.**

## Home Assistant como recurso...

1. Accede a tu panel de control de Pangolin y añade un nuevo recurso llamado `Home Assistant`. Selecciona el sitio correcto, que haga referencia a la instancia de Home Assistant Newt que has definido en los requisitos previos, y asigna un subdominio a tu recurso.
2. Asegúrate de que la opción «Activar SSL» esté marcada para obtener un certificado SSL generado automáticamente que cifre las conexiones del navegador.
3. En la sección «Configuración de destino», añade un destino con el método `HTTP`, el dominio `homeassistant.local.hass.io` y el puerto `8123`. Haz clic en «Añadir destino» y guarda la configuración.
5. Visita la [documentación de Home Assistant](https://www.home-assistant.io/integrations/http) y sigue las instrucciones para añadir un `trusted_proxy` a tu archivo `configuration.yaml`. Probablemente será `172.30.33.0/24`. Asegúrate de establecer también `use_x_forwarded_for: true`, para que en tus registros aparezca la dirección IP del cliente y no la del proxy inverso. Reinicia Home Assistant.
7. (Opcional) Si deseas un recurso que haga referencia a un complemento de Home Assistant, utiliza el slug del complemento en la sección «domain» o en el área «Target configuration». Lo encontrarás en la página de configuración del complemento en Home Assistant. En este ejemplo, el slug es «a0d7b954_tailscale». Si hay un `_`, como en este ejemplo, debe sustituirse por un `-`. Por lo tanto, el dominio correcto para este ejemplo sería `a0d7b954-tailscale`. El puerto depende del complemento; deberá consultar la documentación o la configuración del mismo.

## Configuración

| Opción | Campo obligatorio | Descripción |
|---|---|---|
| `endpoint` | ✅ | URL de tu servidor Pangolin, p. ej., `https://app.pangolin.net` |
| `id` | ✅ | ID de Newt del panel de control de Pangolin |
| `secret` | ✅ | Secreto de Newt del panel de control de Pangolin |
| `log_level` | ❌ | Nivel de registro: `trace`, `debug`, `info`, `warn`, `error` (por defecto: `info`) |
| `docker_socket` | ❌ | Ruta del socket de Docker para la extracción de etiquetas, p. ej., `/var/run/docker.sock` – véase [la documentación](https://docs.pangolin.net/manage/sites/configure-site#docker-socket-integration) |
| `docker_enforce_network_validation` | ❌ | Forzar la validación de red de Docker (por defecto: `false`) |
| `dns` | ❌ | Servidor DNS para la resolución del punto final. (Por defecto: `9.9.9.9`) |
| `disable_clients` | ❌ | Desactivar los clientes en la interfaz de WireGuard. (Por defecto: `false`) |
| `disable_ssh` | ❌ | Desactivar los demonios de autenticación SSH y el modo SSH nativo (por defecto: `false`) |
| `no_cloud` | ❌ | No se puede pasar a la nube si se utilizan nodos gestionados en Pangolin Cloud (por defecto: `false`) |
| `ping_interval` | ❌ | Intervalo para enviar pings al servidor (por defecto: `15s`) |
| `ping_timeout` | ❌ | Tiempo de espera para cada ping (por defecto: `7s`) |
| `tls_client_cert_file` | ❌ | Ruta al archivo de certificado de cliente (formato PEM/DER) para mTLS |
| `tls_client_key` | ❌ | Ruta al archivo de la clave privada del cliente (formato PEM/DER) para mTLS |
| `tls_client_ca` | ❌ | Ruta al archivo de certificado de la CA para la validación de certificados remotos (se puede especificar varias veces) |
| `udp_proxy_idle_timeout string` | ❌ | Tiempo de espera de inactividad para los flujos del cliente del proxy UDP antes de la limpieza (equivale a ). (Por defecto: `90s`) |
| `interface` | ❌ | Nombre de la interfaz de WireGuard (por defecto: `newt`) |
| `mtu` | ❌ | MTU para la interfaz interna de WireGuard. (Por defecto: `1280`) |
| `native` | ❌ | Usar la interfaz nativa de WireGuard (por defecto: `false`) |
| `metrics` | ❌ | Activar el exportador de métricas de Prometheus (por defecto: `false`) |
| `metrics_admin_addr` | ❌ | Asignar una dirección para el administrador/las métricas (por defecto: `127.0.0.1:2112`) |
| `metrics_async_bytes` | ❌ | Activar el recuento asíncrono de bytes (actualización en segundo plano; menor sobrecarga en la ruta activa, según corresponda) (por defecto: `false`) |
| `health_file` | ❌ | Ruta al archivo de estado para la supervisión de la conexión |
| `prefer_endpoint` | ❌ | Dar preferencia a este punto final para la conexión (si se establece, anulará el punto final del servidor) |
| `region` | ❌ | Atributo opcional de recursos de región para telemetría y métricas |
| `name` | ❌ | Nombre del sitio al realizar el aprovisionamiento con una clave de aprovisionamiento |
| `blueprint_file` | ❌ | Ruta al archivo de blueprint para definir los recursos y las configuraciones de Pangolin |
| `provisioning_blueprint_file` | ❌ | Ruta a un archivo de blueprint utilizado únicamente para el arranque |
| `config_file` | ❌ | Ruta al archivo de configuración JSON en el que Newt carga y almacena los ajustes |
| `ad_ca_cert_path` | ❌ | Ruta al archivo de certificado de CA para el daemon de autenticación (por defecto: `/etc/ssh/ca.pem`) |
| `ad_generate_random_password` | ❌ | Generar una contraseña aleatoria para los usuarios autenticados (por defecto: `false`) |
| `ad_pre_shared_key` | ❌ | Clave precompartida para la autenticación del daemon de autenticación. |
| `ad_principals_file` | ❌ | Ruta al archivo de entidades para el daemon de autenticación (por defecto: `/var/run/auth-daemon/principals`) |
| `enforce_hc_cert` | ❌ | Forzar la validación de certificados para las comprobaciones de estado (por defecto: `false`) |
| `port` | ❌ | Puerto para que los pares se conecten a Newt |
| `pprof` | ❌ | Activar los puntos finales de depuración de pprof en el servidor de administración (por defecto: `false`) |
| `otlp` | ❌ | Activar los exportadores OTLP (métricas/trazas) (por defecto: `false`) |
| `updown` | ❌ | Ruta al script de Updown para eventos de adición/eliminación de destinos (por defecto: `false`) |


### Ejemplo de configuración

```yaml
endpoint: "https://app.pangolin.net"
id: "mi-id-newt"
secret: "mi-secreto-newt"
log_level: "info"
```

Nota sobre el procesamiento de opciones

- Las opciones de cadena se pasan a `newt` como `--flag value`.
- Las opciones booleanas se establecen como indicador (`--flag`) cuando son `true`.

CA(s) de TLS

`tls_client_ca` puede especificarse como una sola cadena o como una lista YAML. Ejemplos:

```yaml
# un único archivo
tls_client_ca: "/etc/ssl/ca.pem"

# varios archivos
tls_client_ca:
  - "/etc/ssl/ca.pem"
  - "/etc/ssl/extra-ca.pem"
```

Las entradas se pasan a `newt` como una bandera `--tls-client-ca` cada una.

## Requisitos previos

- Un servidor [Pangolin](https://github.com/fosrl/pangolin) en ejecución
- Un sitio registrado en Pangolin con un Newt-ID y un secreto
- Acceso a la red del host y permisos de WireGuard en el host de Home Assistant

## Cómo encontrar el `newt_id` y el `newt_secret`

1. Abre el panel de control de Pangolin.
2. Selecciona el sitio deseado o crea uno nuevo.
3. Copia el `newt_id` y el `newt_secret` generados de los datos de acceso del sitio.
4. Utiliza el mismo `pangolin_endpoint` que está configurado en tu instalación de Pangolin.

## Notas

- El complemento utiliza `host_network` para que el túnel pueda funcionar directamente a través de la red del host.
- Requiere los permisos `NET_ADMIN` y `SYS_MODULE`.
- Tras realizar cambios en la configuración, es necesario reiniciar el complemento.
- `newt_id` y `newt_secret` deben pertenecer al mismo sitio de Pangolin.
- No compartas `newt_secret` con personas no autorizadas.

## Cómo funciona

Newt se conecta al servidor de Pangolin a través de WebSocket y crea un túnel WireGuard en el espacio de usuario. Todas las conexiones TCP/UDP proxy se reenvían a servicios locales sin necesidad de WireGuard en el kernel ni de complejas reglas de enrutamiento NAT.

## Solución de problemas

- Comprueba los registros del complemento si falla el inicio.
- Asegúrate de que `pangolin_endpoint` sea accesible y utilice un certificado TLS válido.
- Asegúrate de que `newt_id` y `newt_secret` procedan correctamente del mismo sitio de Pangolin.
- Establece `log_level` en `debug` para obtener información más detallada.
- Si modificas la configuración, detén completamente el complemento y reinícialo.

## Más información

- [Configuración del sitio de Pangolin](https://docs.pangolin.net/manage/sites/configure-site)
- [Repositorio de Newt en GitHub](https://github.com/fosrl/newt)
- [Versión 1.13.0 de Newt](https://github.com/fosrl/newt/releases/tag/1.13.0)
