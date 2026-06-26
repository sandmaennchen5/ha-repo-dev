### Home Assistant Add-On: Documentation
## Newt Client for Pangolin Reverse Proxy Tunnels

The [Fossorial system—with Pangolin](https://docs.fossorial.io/) as its core component—is a self-hosted, tunneled reverse proxy with identity and access management, designed to securely deliver private resources via encrypted WireGuard tunnels in user space. Think of it as self-hosted Cloudflare tunnels.

Newt is the main client that connects to Pangolin and enables access to services on the same network as Newt. Install this and connect to your Pangolin instance to enable remote access to Home Assistant via secure WireGuard tunnels.

## Installation

1. Open Home Assistant.
2. Go to **Settings → Add-ons → Add-on Store → ⋮ → Repositories**.
3. Add the repository.
4. Install the **Newt** add-on.
5. Configure the add-on options.
6. Start the add-on.

Enable Newt to access the Docker socket. **You must disable “Protection Mode” on the add-on’s main page.**

## Home Assistant as a Resource...

1. Go to your Pangolin dashboard and add a new resource named `Home Assistant`. Select the correct site corresponding to the Home Assistant Newt instance you defined in the prerequisites, and assign a subdomain to your resource.
2. Make sure the “Enable SSL” option is checked so that you receive an automatically generated SSL certificate to encrypt browser connections.
3. In the “Target Configuration” section, add a target with the method `HTTP`, the domain `homeassistant.local.hass.io`, and the port `8123`. Click “Add Target” and save the settings.
5. Visit the [Home Assistant documentation](https://www.home-assistant.io/integrations/http) and follow the instructions to add a `trusted_proxy` to your `configuration.yaml` file. This is likely `172.30.33.0/24`. Make sure to also set `use_x_forwarded_for: true` so that the client’s IP address appears in your logs instead of the reverse proxy’s IP address. Restart Home Assistant.
7. (Optional) If you want a resource that references a Home Assistant add-on, use the add-on’s slug in the “domain” section or in the “Target configuration” area. You can find this on the add-on’s configuration page in Home Assistant. In this example, the slug is “a0d7b954_tailscale.” If there is an `_`, as in this example, it must be replaced with a `-`. The correct domain for this example would therefore be `a0d7b954-tailscale`. Your port depends on the add-on; you’ll need to consult the add-on’s documentation or configuration.

## Configuration

| Option | Required | Description |
|---|---|---|
| `endpoint` | ✅ | URL of your Pangolin server, e.g., `https://app.pangolin.net` |
| `id` | ✅ | Newt ID from the Pangolin dashboard |
| `secret` | ✅ | Newt secret from the Pangolin dashboard |
| `log_level` | ❌ | Log level: `trace`, `debug`, `info`, `warn`, `error` (default: `info`) |
| `docker_socket` | ❌ | Docker socket path for label scraping, e.g., `/var/run/docker.sock` – see [documentation](https://docs.pangolin.net/manage/sites/configure-site#docker-socket-integration) |
| `docker_enforce_network_validation` | ❌ | Enforce Docker network validation (default: `false`) |
| `dns` | ❌ | DNS server for resolving the endpoint. (Default: `9.9.9.9`) |
| `disable_clients` | ❌ | Disable clients on the WireGuard interface. (Default: `false`) |
| `disable_ssh` | ❌ | Disable SSH authentication daemons and native SSH mode (default: `false`) |
| `no_cloud` | ❌ | You cannot migrate to the cloud if you are using managed nodes in Pangolin Cloud (default: `false`) |
| `ping_interval` | ❌ | Interval for pinging the server (default: `15s`) |
| `ping_timeout` | ❌ | Timeout for each ping (default: `7s`) |
| `tls_client_cert_file` | ❌ | Path to the client certificate file (PEM/DER format) for mTLS |
| `tls_client_key` | ❌ | Path to the client private key file (PEM/DER format) for mTLS |
| `tls_client_ca` | ❌ | Path to the CA certificate file for validating remote certificates (can be specified multiple times) |
| `udp_proxy_idle_timeout string` | ❌ | Idle timeout for UDP proxy client flows before cleanup (equivalent to ). (Default: `90s`) |
| `interface` | ❌ | Name of the WireGuard interface (default: `newt`) |
| `mtu` | ❌ | MTU for the internal WireGuard interface. (Default: `1280`) |
| `native` | ❌ | Use native WireGuard interface (Default: `false`) |
| `metrics` | ❌ | Enable Prometheus /metrics exporter (default: `false`) |
| `metrics_admin_addr` | ❌ | Bind admin/metrics to an address (default: `127.0.0.1:2112`) |
| `metrics_async_bytes` | ❌ | Enable asynchronous byte counting (background flushing; lower hot-path overhead, accordingly) (default: `false`) |
| `health_file` | ❌ | Path to the health file for connection monitoring |
| `prefer_endpoint` | ❌ | Prefer this endpoint for the connection (if set, will override the endpoint from the server) |
| `region` | ❌ | Optional region resource attribute for telemetry and metrics |
| `name` | ❌ | Site name when provisioning with a provisioning key |
| `blueprint_file` | ❌ | Path to the blueprint file defining Pangolin resources and configurations |
| `provisioning_blueprint_file` | ❌ | Path to a blueprint file used only for bootstrapping |
| `config_file` | ❌ | Path to the JSON configuration file where Newt loads and stores settings |
| `ad_ca_cert_path` | ❌ | Path to the CA certificate file for the Auth Daemon (default: `/etc/ssh/ca.pem`) |
| `ad_generate_random_password` | ❌ | Generate a random password for authenticated users (default: `false`) |
| `ad_pre_shared_key` | ❌ | Pre-shared key for Auth Daemon authentication. |
| `ad_principals_file` | ❌ | Path to the principals file for Auth Daemon (default: `/var/run/auth-daemon/principals`) |
| `enforce_hc_cert` | ❌ | Enforce certificate validation for health checks (default: `false`) |
| `port` | ❌ | Port for peers to connect to Newt |
| `pprof` | ❌ | Enable pprof debug endpoints on the admin server (default: `false`) |
| `otlp` | ❌ | Enable OTLP exporters (metrics/traces) (default: `false`) |
| `updown` | ❌ | Path to the Updown script for target add/remove events (default: `false`) |


### Sample Configuration

```yaml
endpoint: "https://app.pangolin.net"
id: "my-newt-id"
secret: "my-newt-secret"
log_level: "info"
```

Note on Option Processing

- String options are passed to `newt` as `--flag value`.
- Boolean options are set as a flag (`--flag`) if they are `true`.

TLS CA(s)

`tls_client_ca` can be specified either as a single string or as a YAML list. Examples:

```yaml
# single file
tls_client_ca: "/etc/ssl/ca.pem"

# multiple files
tls_client_ca:
  - "/etc/ssl/ca.pem"
  - "/etc/ssl/extra-ca.pem"
```

The entries are passed to `newt` as individual `--tls-client-ca` flags.

## Prerequisites

- A running [Pangolin](https://github.com/fosrl/pangolin) server
- A site registered in Pangolin with a Newt ID and secret
- Host network access and WireGuard permissions on the Home Assistant host

## How to find `newt_id` and `newt_secret`

1. Open the Pangolin dashboard.
2. Select the desired site or create a new one.
3. Copy the generated `newt_id` and `newt_secret` from the site credentials.
4. Use the same `pangolin_endpoint` that is configured in your Pangolin installation.

## Notes

- The add-on uses `host_network` so that the tunnel can be operated directly over the host network.
- It requires the `NET_ADMIN` and `SYS_MODULE` permissions.
- The add-on must be restarted after making changes to the configuration.
- `newt_id` and `newt_secret` must belong to the same Pangolin site.
- Do not share `newt_secret` with unauthorized individuals.

## How It Works

Newt connects to the Pangolin server via WebSocket and creates a WireGuard tunnel in user space. All proxied TCP/UDP connections are forwarded to local services without requiring kernel-level WireGuard or complex NAT routing rules.

## Troubleshooting

- Check the add-on logs if startup fails.
- Make sure that `pangolin_endpoint` is reachable and uses a valid TLS certificate.
- Make sure that `newt_id` and `newt_secret` are correctly sourced from the same Pangolin site.
- Set `log_level` to `debug` to get more detailed information.
- If you change the configuration, stop the add-on completely and restart it.

## Further Information

- [Pangolin Site Configuration](https://docs.pangolin.net/manage/sites/configure-site)
- [Newt GitHub Repository](https://github.com/fosrl/newt)
- [Newt Release 1.13.0](https://github.com/fosrl/newt/releases/tag/1.13.0)
