from pathlib import Path

from utils import (
    load_yaml,
    load_config_sections,
    resolve_source,
    build_badge_url,
    build_custom_shield,
    render_markdown,
    apply_case,
    apply_template,
    apply_transforms,
    encode_shields
)

from plugin_loader import load_plugin

CONFIG_FILE = ".github/config.yaml"
APPS_DIR = Path("apps")


def load_badge_config():
    badge_section, _ = load_config_sections()
    return badge_section


def load_defaults():
    return load_badge_config().get("defaults", {})


def load_badges():
    return load_badge_config().get("badges", {})


def load_groups():
    return load_badge_config().get("groups", {})


def load_app(app_path):

    config = load_yaml(app_path / "config.yaml")
    var = load_yaml(app_path / ".var.yaml")

    return {"app": config, "var": var}


def get_apps():

    apps = []

    if not APPS_DIR.exists():
        return apps

    for app_dir in APPS_DIR.iterdir():

        if app_dir.is_dir() and (app_dir / "config.yaml").exists():
            apps.append(app_dir)

    apps.sort(
        key=lambda d: load_yaml(d / "config.yaml").get("name", d.name).lower()
    )

    return apps


def is_hidden(badge_id, group, app_data):

    hidden_badges = app_data["var"].get("hide_badges", [])

    if badge_id in hidden_badges:
        return True

    hidden_groups = app_data["var"].get("hide_groups", [])

    return group in hidden_groups


def apply_override(badge_id, group, badge, app_data):

    group_overrides = app_data["var"].get("group_overrides", {})

    if group in group_overrides:
        badge.update(group_overrides[group])

    badge_overrides = app_data["var"].get("badge_overrides", {})

    if badge_id in badge_overrides:
        badge.update(badge_overrides[badge_id])

    return badge


def build_variables(badge_id, group, label, value, color, style, app_data, definition):

    return {
        "id": badge_id,
        "group": group,
        "label": label,
        "value": value,
        "color": color,
        "style": style,
        "name": app_data["app"].get("name", ""),
        "slug": app_data["app"].get("slug", ""),
        "version": app_data["app"].get("version", ""),
        "description": app_data["app"].get("description", ""),
        "repo": definition.get("repo", "")
    }


def build_badge(badge_id, definition, app_data):

    defaults = load_defaults()

    if not definition.get("enabled", True):
        return None

    label = definition.get("label", badge_id)
    color = definition.get("color", defaults.get("color", "blue"))
    style = definition.get("style", defaults.get("style", "flat-square"))
    group = definition.get("group", "default")
    order = definition.get("order", 100)

    badge_type = definition.get("type", "field")
    value = ""

    if badge_type == "field":

        value = resolve_source(app_data, definition["source"])

    elif badge_type == "bool":

        state = resolve_source(app_data, definition["source"])

        if state:
            value = definition.get("text_true", "true")
            color = definition.get("color_true", "brightgreen")
        else:
            value = definition.get("text_false", "false")
            color = definition.get("color_false", "red")

    elif badge_type == "list":

        values = resolve_source(app_data, definition["source"])

        if values is None:
            values = []

        if not isinstance(values, list):
            values = [str(values)]

        separator = definition.get("separator", defaults.get("separator", ", "))
        value = separator.join(map(str, values))

    elif badge_type == "text":

        value = definition.get("text", "")

    elif badge_type == "plugin":

        plugin = load_plugin(definition["plugin"])
        result = plugin.generate(app_data, definition)
        value = result.get("value", "")
        color = result.get("color", color)

    # Apply transform pipeline
    transforms = definition.get("transforms", [])

    if transforms:
        value = apply_transforms(value, transforms)

    # After transforms value should be a string
    if isinstance(value, list):
        sep = definition.get("separator", defaults.get("separator", ", "))
        value = sep.join(map(str, value))

    if value in ("", None):

        if "fallback" in definition:
            value = definition["fallback"]
        else:
            value = definition.get("empty_value", "")

        if value == "" and not definition.get("show_empty", True):
            return None

    value = apply_case(
        value,
        definition.get("uppercase", False),
        definition.get("lowercase", False)
    )

    value = apply_template(
        value,
        definition.get("prefix", ""),
        definition.get("suffix", ""),
        definition.get("template", "{prefix}{value}{suffix}")
    )

    variables = build_variables(badge_id, group, label, value, color, style, app_data, definition)

    query = {}
    query.update(defaults.get("query", {}))
    query.update(definition.get("query", {}))

    shield = definition.get("shield")
    shields = defaults.get("shields", {})

    logo = definition.get("logo")
    logo_color = definition.get("logoColor")
    logo_url = definition.get("logoUrl")

    # When transforms are defined the user already prepared the value; skip
    # DEFAULT_REPLACEMENTS to avoid double-encoding. Pass {} = no str replacements.
    has_transforms = bool(transforms)
    explicit_replacements = defaults.get("replacements")
    if has_transforms:
        effective_replacements = explicit_replacements if explicit_replacements is not None else {}
    else:
        effective_replacements = explicit_replacements  # None → DEFAULT_REPLACEMENTS inside encode_shields

    if shield:

        if shield.startswith("http") or shield.startswith("{"):
            url = build_custom_shield(shield, {"value": value}, effective_replacements)

        elif shield in shields:
            url = build_custom_shield(
                shields[shield],
                {"value": value},
                effective_replacements
            )

        else:
            url = build_badge_url(
                label, value, color, style,
                logo, logo_color, logo_url, query,
                effective_replacements
            )

    else:
        url = build_badge_url(
            label, value, color, style,
            logo, logo_color, logo_url, query,
            effective_replacements
        )

    markdown = render_markdown(label, url, definition.get("url"))

    badge = {
        "id": badge_id,
        "label": label,
        "value": value,
        "group": group,
        "order": order,
        "url": url,
        "markdown": markdown,
        "color": color
    }

    return apply_override(badge_id, group, badge, app_data)


def generate_app_badges(app_path):

    app_data = load_app(app_path)
    badges = load_badges()
    result = []

    for badge_id, definition in badges.items():

        group = definition.get("group", "default")

        if is_hidden(badge_id, group, app_data):
            continue

        badge = build_badge(badge_id, definition, app_data)

        if badge:
            result.append(badge)

    result.sort(key=lambda x: (x["group"], x["order"]))

    return result


def build_markdown(badges):

    return "\n".join(badge["markdown"] for badge in badges)
