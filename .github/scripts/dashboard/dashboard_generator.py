import bootstrap

from pathlib import Path
import json

from badge_generator import get_apps, load_app, generate_app_badges

from common import (
    ensure_dirs,
    copy_assets,
    export_json,
    load_dashboard_config,
    OUTPUT_DIR
)

from pages import (
    render_index,
    render_matrix,
    render_history,
    render_health,
    render_lab,
    render_app_pages,
    render_apps_index,
    render_badge_pages,
    render_app_history_pages,
    render_settings,
    render_badges
)

EMPTY_VALUES = {"", "none", "null", "-", "n/a"}


def load_history():

    file = OUTPUT_DIR / "data" / "history.json"

    if not file.exists():
        return []

    with open(file, encoding="utf-8") as f:
        return json.load(f)


def score_badges(badges):

    green = yellow = red = 0
    real_badges = 0

    for badge in badges:

        value = str(badge.get("value", "")).strip().lower()

        if value not in EMPTY_VALUES:
            real_badges += 1

        color = badge.get("color", "").lower()

        if color in ("green", "brightgreen"):
            green += 1
        elif color in ("yellow", "blue", "informational", "orange", "grey", "gray", "lightgrey"):
            yellow += 1
        elif color in ("red", "critical"):
            red += 1

    total = green + yellow + red
    score = round((green * 100 + yellow * 50) / total) if total > 0 else 100

    return green, yellow, red, score, real_badges


def build_apps():

    result = []

    for app_path in get_apps():

        app = load_app(app_path)
        badges = generate_app_badges(app_path)
        green, yellow, red, score, real_badges = score_badges(badges)

        result.append({
            "slug": app_path.name,
            "name": app["app"].get("name", app_path.name),
            "description": app["app"].get("description", ""),
            "version": app["app"].get("version", ""),
            "badges": badges,
            "real_badges": real_badges,
            "green": green,
            "yellow": yellow,
            "red": red,
            "score": score
        })

    return result


def main():

    ensure_dirs()

    config = load_dashboard_config()
    apps = build_apps()
    history = load_history()

    copy_assets()

    export_json("apps.json", apps)

    badges = []

    for app in apps:
        for badge in app.get("badges", []):
            value = str(badge.get("value", "")).strip()
            badges.append({
                "app": app.get("slug"),
                "app_name": app.get("name"),
                "label": badge.get("label", ""),
                "value": badge.get("value", ""),
                "color": badge.get("color", ""),
                "status": "OK" if value.lower() not in EMPTY_VALUES else "NO_DATA"
            })

    export_json("badges.json", badges)

    stats = {
        "apps": len(apps),
        "badges": sum(a["real_badges"] for a in apps),
        "green": sum(a["green"] for a in apps),
        "yellow": sum(a["yellow"] for a in apps),
        "red": sum(a["red"] for a in apps),
        "health_score": round(sum(a["score"] for a in apps) / len(apps)) if apps else 0
    }

    render_index(config, apps, stats)
    render_matrix(config, apps)
    render_health(config, apps, stats)
    render_history(config, history)
    render_lab(config)
    render_app_pages(config, apps)
    render_apps_index(config, apps)
    render_badge_pages(config, apps)
    render_app_history_pages(config, apps, history)
    render_settings(config)
    render_badges(config, badges)


if __name__ == "__main__":
    main()
