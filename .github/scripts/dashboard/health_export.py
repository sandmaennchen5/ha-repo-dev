import bootstrap

from pathlib import Path
import json

from health_check import run_health

OUTPUT_DIR = Path(".dashboard/data")


def ensure_dirs():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():

    ensure_dirs()

    health = run_health()

    with open(OUTPUT_DIR / "health.json", "w", encoding="utf-8") as f:
        json.dump(health, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
