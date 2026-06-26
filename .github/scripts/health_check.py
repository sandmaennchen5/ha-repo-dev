from pathlib import Path
import sys

from utils import load_yaml, load_config_sections

ROOT_README = Path("README.md")
APPS_DIR = Path("apps")

VALID_STYLES = {"flat", "flat-square", "plastic", "for-the-badge", "social"}


def warning(app, message):
    return {"type": "WARNING", "app": app, "message": message}


def error(app, message):
    return {"type": "ERROR", "app": app, "message": message}


def get_apps():

    apps = []

    if not APPS_DIR.exists():
        return apps

    for app_dir in APPS_DIR.iterdir():

        if app_dir.is_dir() and (app_dir / "config.yaml").exists():
            apps.append(app_dir)

    return apps


def load_badge_config():
    badge_section, _ = load_config_sections()
    return badge_section


def check_root_readme():

    result = []

    if not ROOT_README.exists():
        result.append(error("root", "README.md missing"))
        return result

    text = ROOT_README.read_text(encoding="utf-8")

    if "<!-- APPS-LIST-START -->" not in text:
        result.append(warning("root", "APPS-LIST marker missing"))

    return result


def check_app_readme(app_dir):

    result = []
    readme = app_dir / "README.md"

    if not readme.exists():
        result.append(warning(app_dir.name, "README.md missing"))
        return result

    text = readme.read_text(encoding="utf-8")

    if "<!-- BADGES-START -->" not in text:
        result.append(warning(app_dir.name, "BADGES marker missing"))

    return result


def check_groups():

    result = []
    data = load_badge_config()
    groups = data.get("groups", {})
    badges = data.get("badges", {})

    for badge_id, badge in badges.items():

        group = badge.get("group", "default")

        if group not in groups:
            result.append(error(badge_id, f"unknown group '{group}'"))

    return result


def check_styles():

    result = []
    badges = load_badge_config().get("badges", {})

    for badge_id, badge in badges.items():

        style = badge.get("style")

        if style and style not in VALID_STYLES:
            result.append(warning(badge_id, f"unknown style '{style}'"))

    return result


def check_group_overrides():

    result = []
    groups = load_badge_config().get("groups", {})

    for app_dir in get_apps():

        var = load_yaml(app_dir / ".var.yaml")

        for group in var.get("group_overrides", {}):

            if group not in groups:
                result.append(warning(app_dir.name, f"group override '{group}' unknown"))

    return result


def check_hide_groups():

    result = []
    groups = load_badge_config().get("groups", {})

    for app_dir in get_apps():

        var = load_yaml(app_dir / ".var.yaml")

        for group in var.get("hide_groups", []):

            if group not in groups:
                result.append(warning(app_dir.name, f"hidden group '{group}' unknown"))

    return result


def run_health():

    result = []

    result.extend(check_root_readme())
    result.extend(check_groups())
    result.extend(check_styles())
    result.extend(check_group_overrides())
    result.extend(check_hide_groups())

    for app_dir in get_apps():
        result.extend(check_app_readme(app_dir))

    return result


def main():

    items = run_health()

    if not items:
        print("Health check passed. No issues found.")
        return

    for item in items:
        print(f"[{item['type']}] {item['app']}: {item['message']}")

    errors = [i for i in items if i["type"] == "ERROR"]

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
