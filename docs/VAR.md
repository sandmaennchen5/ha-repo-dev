# .var.yaml Referenz

Die `.var.yaml` Datei enthält technische Metadaten, die Home Assistant nicht kennt.

## Alle Felder

```yaml
# ── Darstellung ─────────────────────────────────────────────────
hidden: false          # App aus Root-README ausblenden
icon: "🛰️"            # Emoji vor dem App-Namen in der README-Liste
stage: "stable"        # stable | beta | lab

# ── README-Kontrolle ────────────────────────────────────────────
hide_root_readme: false    # Nicht in Haupt-README anzeigen
hide_app_readme: false     # Badges in App-README nicht aktualisieren

# ── Badge-Kontrolle ─────────────────────────────────────────────
hide_badges:
  - python_version         # Badge-IDs aus config.yaml

hide_groups:
  - upstream               # Gruppen-IDs aus config.yaml

# ── Badge-Overrides (App-spezifisch) ────────────────────────────
badge_overrides:
  version:
    color: orange
    prefix: "v"
    logo: github

group_overrides:
  security:
    style: for-the-badge

# ── Upstream ────────────────────────────────────────────────────
upstream_version: "1.2.3"
upstream_repo: "github.com/owner/repo"
upstream_commit: "abc1234"

# ── Build / Lint / QA ───────────────────────────────────────────
build: "passing"
lint: "passing"
yaml_lint: "passing"
code_quality: "A"

# ── System ──────────────────────────────────────────────────────
image_size: "45MB"

# ── Custom Badges ───────────────────────────────────────────────
custom_shield: "https://img.shields.io/badge/tunnel-secure-blue"
custom_flag: "secure"

# ── Meta ────────────────────────────────────────────────────────
updated: "2026-06-26"    # YYYY-MM-DD
source: "github.com/owner/repo"
```
