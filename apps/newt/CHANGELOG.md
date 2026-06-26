# Changelog

Alle wichtigen Änderungen für das Newt Add-on.

## [1.13.0] - 2026-06-10

### Was ist neu

- Add browser gateway support for VNC, RDP, and SSH
- Add native internal ssh server for easier ssh private resources
- Add `--disable-ssh` flag to replace `--auth-daemon` which is now enabled by default
- Add auto update newt support when running as binary
- Add advantech router app
- Add SIGHUP support to reload config
- Add `block` flag to block all connections to config
- Add restart endpoint

### Fehlerbehebungen

- Fix `X-Forwarded-Proto` always set to `http` for TLS connections
- Fix duplicate wrong error log in `socket/fetch`
- Fix dead code in `reliablePing`
- Dependency security updates

### Beiträge

- Neue Mitwirkende: @rinseaid, @cwiggs, @immanuwell, @eleboucher

### Assets

- GHCR: `ghcr.io/fosrl/newt@sha256:63d956c8fdee889255e441ec405193b47b1fd2d975b505492ec848a8007f4fc3`
- Docker Hub: `docker.io/fosrl/newt@sha256:63d956c8fdee889255e441ec405193b47b1fd2d975b505492ec848a8007f4fc3`
- Tag: `1.13.0`

---

Weitere Informationen: https://github.com/fosrl/newt/releases/tag/1.13.0
