# Schema-Validierung

Die Schema-Validierung erfolgt automatisch im `badge-lint.yml` Workflow und kann lokal ausgeführt werden:

```bash
cd .github/scripts
pip install pyyaml jsonschema
python schema_validator.py
```

## Schemata

| Datei | Schema | Beschreibung |
|-------|--------|-------------|
| `.github/config.yaml` | `badges.schema.json` | Badge-Konfiguration |
| `apps/*/config.yaml` | `config.schema.json` | App-Konfiguration (HA-Felder) |
| `apps/*/.var.yaml` | `var.schema.json` | Technische Metadaten |

## badges.schema.json

Validiert den Badge-Abschnitt der `.github/config.yaml`. Stellt sicher, dass:
- Alle Badges einen `type` haben
- Transforms gültige Typen haben

## config.schema.json

Validiert die HA-App-Konfiguration. Pflichtfelder: `name`.

## var.schema.json

Validiert die technischen Metadaten einer App.
