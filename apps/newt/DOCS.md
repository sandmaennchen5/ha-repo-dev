### Home Assistant Add-On: Dokumentation test
## Newt Client für Pangolin-Reverse-Proxy-Tunnel

Das [Fossorial-System – mit Pangolin](https://docs.fossorial.io/) als Kernkomponente – ist ein selbst gehosteter, getunnelter Reverse-Proxy mit Identitäts- und Zugriffsmanagement, der entwickelt wurde, um private Ressourcen sicher über verschlüsselte WireGuard-Tunnel im Userspace bereitzustellen. Stellen Sie sich das wie selbst gehostete Cloudflare-Tunnel vor.

Newt ist der Hauptclient, der eine Verbindung zu Pangolin herstellt und den Zugriff auf Dienste im selben Netzwerk wie Newt ermöglicht. Installieren Sie dies und verbinden Sie sich mit Ihrer Pangolin-Instanz, um den Fernzugriff auf Home Assistant über sichere WireGuard-Tunnel zu ermöglichen

## Installation

1. Öffne Home Assistant.
2. Gehe zu **Einstellungen → Add-ons → Add-on Store → ⋮ → Repositories**.
3. Füge das Repository hinzu.
4. Installiere das Add-on **Newt**.
5. Konfiguriere die Add-on-Optionen.
6. Starte das Add-on.

Ermöglicht Newt den Zugriff auf den Docker-Socket. **Sie müssen den „Schutzmodus“ auf der Hauptseite des Add-ons deaktivieren.**

## Home Assitant als Resource..

1. Rufen Sie Ihr Pangolin-Dashboard auf und fügen Sie eine neue Ressource namens `Home Assistant` hinzu. Wählen Sie die richtige Site aus, die sich auf die Home Assistant Newt-Instanz bezieht, die Sie in den Voraussetzungen definiert haben, und geben Sie Ihrer Ressource eine Subdomain.
2. Stelle sicher, dass die Option „SSL aktivieren“ aktiviert ist, damit du ein automatisch generiertes SSL-Zertifikat zur Verschlüsselung der Browserverbindungen erhältst.
3. Fügen Sie im Bereich „Zielkonfiguration“ ein Ziel mit der Methode `HTTP`, der Domain `homeassistant.local.hass.io` und dem Port `8123` hinzu. Klicken Sie auf „Ziel hinzufügen“ und speichern Sie die Einstellungen.
5. Besuche die [Home Assistant-Dokumentation](https://www.home-assistant.io/integrations/http) und befolge die Anweisungen, um einen `trusted_proxy` zu deiner `configuration.yaml`-Datei hinzuzufügen. Dieser lautet wahrscheinlich `172.30.33.0/24`. Stellen Sie sicher, dass Sie auch `use_x_forwarded_for: true` setzen, damit die IP-Adresse des Clients in Ihren Protokollen erscheint und nicht die IP-Adresse des Reverse-Proxys. Starten Sie Home Assistant neu.
7. (Optional) Wenn Sie eine Ressource wünschen, die auf ein Home Assistant-Add-on verweist, verwenden Sie im Abschnitt „domain“ oder im Bereich „Target configuration“ den Slug des Add-ons. Sie finden diesen auf der Add-on-Konfigurationsseite in Home Assistant. In diesem Beispiel lautet der Slug „a0d7b954_tailscale“. Wenn ein `_` vorhanden ist, wie in diesem Beispiel, muss es durch ein `-` ersetzt werden. Die korrekte Domain für dieses Beispiel wäre also `a0d7b954-tailscale`. Ihr Port hängt vom Add-on ab; Sie müssen die Dokumentation oder Konfiguration des Add-ons zu Rate ziehen.

## Konfiguration

| Option | Pflichtfeld | Beschreibung |
|---|---|---|
| `endpoint` | ✅ | URL deines Pangolin-Servers, z. B. `https://app.pangolin.net` |
| `id` | ✅ | Newt-ID aus dem Pangolin-Dashboard |
| `secret` | ✅ | Newt-Secret aus dem Pangolin-Dashboard |
| `log_level` | ❌ | Log-Level: `trace`, `debug`, `info`, `warn`, `error` (Standard: `info`) |
| `docker_socket` | ❌ | Docker-Socket-Pfad für Label-Scraping, z. B. `/var/run/docker.sock` – siehe [Dokumentation](https://docs.pangolin.net/manage/sites/configure-site#docker-socket-integration) |
| `docker_enforce_network_validation` | ❌ | Docker-Netzwerk-Validierung erzwingen (Standard: `false`) |
| `dns` | ❌ | DNS-Server zur Auflösung des Endpunkts. (Standard: `9.9.9.9`) |
| `disable_clients` | ❌ | Deaktiviere Clients auf der WireGuard-Schnittstelle. (Standard: `false`) |
| `disable_ssh` | ❌ | Deaktivieren Sie SSH-Authentifizierungsdämonen und den nativen SSH-Modus (Standard: `false`) |
| `no_cloud` | ❌ | Man kann nicht in die Cloud übergehen, wenn man verwaltete Knoten in Pangolin Cloud verwendet (Standard: `false`) |
| `ping_interval` | ❌ | Intervall zum Pingen des Servers (Standard: `15s`) |
| `ping_timeout` | ❌ | Timeout für jeden Ping (Standard: `7s`) |
| `tls_client_cert_file` | ❌ | Pfad zur Client-Zertifikatsdatei (PEM/DER-Format) für mTLS |
| `tls_client_key` | ❌ | Pfad zur Client-Privatschlüsseldatei (PEM/DER-Format) für mTLS |
| `tls_client_ca` | ❌ | Pfad zur CA-Zertifikatsdatei zur Validierung von entfernten Zertifikaten (kann mehrfach angegeben werden) |
| `udp_proxy_idle_timeout string` | ❌ | Idle-Timeout für UDP-Proxy-Client-Flows vor der Bereinigung (entspricht ). (Standard: `90s`) |
| `interface` | ❌ | Name der WireGuard-Schnittstelle (Standard: `newt`) |
| `mtu` | ❌ | MTU für die interne WireGuard-Schnittstelle. (Standard: `1280`) |
| `native` | ❌ | Use native WireGuard interface (Standard: `false`) |
| `metrics` | ❌ | Prometheus /metrics exporter aktivieren (Standard: `false`) |
| `metrics_admin_addr` | ❌ | Admin/Metriken binden eine Adresse (Standard: `127.0.0.1:2112`) |
| `metrics_async_bytes` | ❌ | Aktivieren Sie asynchrone Byte-Zählung (Hintergrundspülung; niedrigere Hot-Path-Overhead, entsprechend ) (Standard: `false`) |
| `health_file` | ❌ | Pfad zur Gesundheitsdatei zur Verbindungsüberwachung |
| `prefer_endpoint` | ❌ | Prefer this endpoint for the connection (if set, will override the endpoint from the server) |
| `region` | ❌ | Optionales Region-Ressourcenattribut für Telemetrie und Metriken |
| `name` | ❌ | Site-Name bei der Bereitstellung mit einem Provisionierungsschlüssel |
| `blueprint_file` | ❌ | Pfad zur Blueprint-Datei zur Definition von Pangolin-Ressourcen und -Konfigurationen |
| `provisioning_blueprint_file` | ❌ | Pfad zu einer nur für Bootstrap verwendeten Blueprint-Datei |
| `config_file` | ❌ | Pfad zur JSON-Konfigurationsdatei, in der Newt Einstellungen lädt und gespeichert wird |
| `ad_ca_cert_path` | ❌ | Pfad zur CA-Zertifikatsdatei für Auth Daemon (Standard: `/etc/ssh/ca.pem`) |
| `ad_generate_random_password` | ❌ | Generiere ein zufälliges Passwort für authentifizierte Nutzer (Standard: `false`) |
| `ad_pre_shared_key` | ❌ | Vor-geteilter Schlüssel zur Auth-Daemon-Authentifizierung. |
| `ad_principals_file` | ❌ | Pfad zur Principals-Datei für Auth Daemon (Standard: `/var/run/auth-daemon/principals`) |
| `enforce_hc_cert` | ❌ | Zertifikatsvalidierung für Gesundheitsprüfungen erzwingen (Standard: `false`) |
| `port` | ❌ | Port für die Peers, um sich mit Newt zu verbinden |
| `pprof` | ❌ | Aktiviere pprof-Debug-Endpunkte auf dem Admin-Server (Standard: `false`) |
| `otlp` | ❌ | Aktivieren Sie OTLP-Exporteure (Metriken/Traces) (Standard: `false`) |
| `updown` | ❌ | Pfad zum Updown-Skript für Ziel-Hinzufügen/Entfernen-Ereignisse (Standard: `false`) |


### Beispielkonfiguration

```yaml
endpoint: "https://app.pangolin.net"
id: "meine-newt-id"
secret: "mein-newt-secret"
log_level: "info"
```

Hinweis zur Optionen-Verarbeitung

- String-Optionen werden als `--flag value` an `newt` übergeben.
- Boolean-Optionen werden als Flag (`--flag`) gesetzt, wenn sie `true` sind.

TLS CA(s)

`tls_client_ca` kann entweder als einzelne Zeichenkette oder als YAML-Liste angegeben werden. Beispiele:

```yaml
# einzelne Datei
tls_client_ca: "/etc/ssl/ca.pem"

# mehrere Dateien
tls_client_ca:
	- "/etc/ssl/ca.pem"
	- "/etc/ssl/extra-ca.pem"
```

Die Einträge werden als je ein `--tls-client-ca` Flag an `newt` übergeben.

## Voraussetzungen

- Ein laufender [Pangolin](https://github.com/fosrl/pangolin)-Server
- Eine in Pangolin registrierte Site mit Newt-ID und Secret
- Host-Netzwerkzugriff und WireGuard-Berechtigungen auf dem Home Assistant Host

## So findest du `newt_id` und `newt_secret`

1. Öffne das Pangolin-Dashboard.
2. Wähle die gewünschte Site aus oder erstelle eine neue.
3. Kopiere die generierte `newt_id` und das `newt_secret` aus den Site-Zugangsdaten.
4. Verwende dasselbe `pangolin_endpoint`, das in deiner Pangolin-Installation konfiguriert ist.

## Hinweise

- Das Add-on nutzt `host_network`, damit der Tunnel direkt über das Host-Netzwerk betrieben werden kann.
- Es benötigt die Berechtigungen `NET_ADMIN` und `SYS_MODULE`.
- Nach Änderungen an der Konfiguration muss das Add-on neu gestartet werden.
- `newt_id` und `newt_secret` müssen zur selben Pangolin-Site gehören.
- Teile `newt_secret` nicht mit unbefugten Personen.

## Wie es funktioniert

Newt verbindet sich per WebSocket mit dem Pangolin-Server und erstellt einen WireGuard-Tunnel im User Space. Alle proxied TCP/UDP-Verbindungen werden an lokale Dienste weitergeleitet, ohne dass Kernel-WireGuard oder komplexe NAT-Routing-Regeln benötigt werden.

## Troubleshooting

- Prüfe die Add-on-Logs, wenn der Start fehlschlägt.
- Stelle sicher, dass `pangolin_endpoint` erreichbar ist und ein gültiges TLS-Zertifikat verwendet.
- Vergewissere dich, dass `newt_id` und `newt_secret` korrekt aus derselben Pangolin-Site stammen.
- Setze `log_level` auf `debug`, um detailliertere Informationen zu erhalten.
- Wenn du die Konfiguration änderst, stoppe das Add-on komplett und starte es neu.

## Weitere Informationen

- [Pangolin Site-Konfiguration](https://docs.pangolin.net/manage/sites/configure-site)
- [Newt GitHub Repository](https://github.com/fosrl/newt)
- [Newt Release 1.13.0](https://github.com/fosrl/newt/releases/tag/1.13.0)
