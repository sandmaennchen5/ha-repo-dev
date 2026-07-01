import bootstrap

from pathlib import Path
import json
from datetime import datetime, timezone

from badge_generator import get_apps, load_app, generate_app_badges

OUTPUT_DIR = Path(".dashboard/data")
HISTORY_DIR = Path(".history")


def ensure_dirs():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def build_snapshot():

    apps = []

    for app_path in get_apps():

        app = load_app(app_path)
        badges = generate_app_badges(app_path)

        green = yellow = red = 0

        for badge in badges:

            color = badge.get("color", "").lower()

            if color in ("green", "brightgreen"):
                green += 1
            elif color in ("yellow", "orange"):
                yellow += 1
            elif color in ("red", "critical"):
                red += 1

        total = green + yellow + red
        score = round((green * 100 + yellow * 50) / total) if total > 0 else 100

        apps.append({
            "slug": app_path.name,
            "name": app["app"].get("name", app_path.name),
            "score": score,
            "green": green,
            "yellow": yellow,
            "red": red,
            "badges": len(badges)
        })

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "apps": apps
    }


def load_history():

    file = HISTORY_DIR / "history.json"

    if not file.exists():
        return []

    with open(file, encoding="utf-8") as f:
        return json.load(f)


def save_history(history):

    with open(HISTORY_DIR / "history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def export_dashboard(history):

    with open(OUTPUT_DIR / "history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def main():

    ensure_dirs()

    history = load_history()
    history.append(build_snapshot())
    history = history[-365:]

    save_history(history)
    export_dashboard(history)


if __name__ == "__main__":
    main()
