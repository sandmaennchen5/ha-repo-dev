from pathlib import Path
import json
import sys
import jsonschema

from utils import load_yaml

SCHEMA_DIR = Path(".github/schema")
APPS_DIR = Path("apps")


def validate_file(yaml_file, schema_file):

    data = load_yaml(yaml_file)

    with open(schema_file, encoding="utf-8") as f:
        schema = json.load(f)

    jsonschema.validate(data, schema)


def validate_config():

    validate_file(
        ".github/config.yaml",
        SCHEMA_DIR / "badges.schema.json"
    )


def validate_apps():

    config_schema = SCHEMA_DIR / "config.schema.json"
    var_schema = SCHEMA_DIR / "var.schema.json"

    for app_dir in APPS_DIR.iterdir():

        if not app_dir.is_dir():
            continue

        config_file = app_dir / "config.yaml"

        if config_file.exists():
            validate_file(config_file, config_schema)

        var_file = app_dir / ".var.yaml"

        if var_file.exists():
            validate_file(var_file, var_schema)


def main():

    try:
        validate_config()
        validate_apps()
        print("Schema validation successful.")
    except jsonschema.ValidationError as e:
        print(f"Schema validation failed: {e.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Validation error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
