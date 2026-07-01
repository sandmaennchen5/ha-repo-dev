from pathlib import Path
import re

from badge_generator import (
    get_apps,
    load_app,
    generate_app_badges,
    build_markdown
)

ROOT_README = Path("README.md")


def replace_marker(text, marker, content):

    start = f"<!-- {marker}-START -->"
    end = f"<!-- {marker}-END -->"

    pattern = rf"{re.escape(start)}.*?{re.escape(end)}"

    replacement = start + "\n" + content + "\n" + end

    return re.sub(pattern, replacement, text, flags=re.DOTALL)


def update_file(path, marker, content):

    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    text = replace_marker(text, marker, content)
    path.write_text(text, encoding="utf-8")


def build_group_markdown(badges, group):

    lines = []

    for badge in badges:

        if badge["group"] == group:
            lines.append(badge["markdown"])

    return "\n".join(lines)


def build_root_section():

    lines = []

    for app_path in get_apps():

        app_data = load_app(app_path)

        if app_data["var"].get("hide_root_readme", False):
            continue

        badges = generate_app_badges(app_path)
        markdown = build_markdown(badges)

        icon = app_data["var"].get("icon", "")
        name = app_data["app"].get("name", app_path.name)
        description = app_data["app"].get("description", "")

        prefix = f"{icon} " if icon else ""

        lines.append(f"## [{prefix}{name}]({app_path.as_posix()}/)")

        if description:
            lines.append("")
            lines.append(description)

        if markdown:
            lines.append("")
            lines.append(markdown)

        lines.append("")

    return "\n".join(lines)


def update_root_readme():

    content = build_root_section()
    update_file(ROOT_README, "APPS-LIST", content)


def update_app_readme(app_path):

    app_data = load_app(app_path)

    if app_data["var"].get("hide_app_readme", False):
        return

    readme = app_path / "README.md"

    if not readme.exists():
        return

    badges = generate_app_badges(app_path)
    text = readme.read_text(encoding="utf-8")

    text = replace_marker(text, "BADGES", build_markdown(badges))

    groups = set(badge["group"] for badge in badges)

    for group in groups:
        text = replace_marker(
            text,
            f"BADGES:{group}",
            build_group_markdown(badges, group)
        )

    readme.write_text(text, encoding="utf-8")


def main():

    update_root_readme()

    for app in get_apps():
        update_app_readme(app)

    print("README generation complete.")


if __name__ == "__main__":
    main()
