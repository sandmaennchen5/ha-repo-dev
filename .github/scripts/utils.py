from pathlib import Path
from urllib.parse import quote, urlencode
import re

import yaml


DEFAULT_REPLACEMENTS = {
    "-": "--",
    " ": "_"
}

CONFIG_FILE = ".github/config.yaml"


def load_yaml(path):

    path = Path(path)

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data or {}


def load_config_sections():
    """Load .github/config.yaml, split at '---' into badge and dashboard sections."""

    path = Path(CONFIG_FILE)

    if not path.exists():
        return {}, {}

    text = path.read_text(encoding="utf-8")

    parts = text.split("\n---\n", 1)

    badge_data = yaml.safe_load(parts[0]) or {}
    dashboard_data = yaml.safe_load(parts[1]) if len(parts) > 1 else {}

    return badge_data, dashboard_data


def resolve_path(data, path):

    current = data

    for part in path.split("."):

        if not isinstance(current, dict):
            return None

        current = current.get(part)

        if current is None:
            return None

    return current


def resolve_source(app_data, source):

    if "." in source:
        return resolve_path(app_data, source)

    value = resolve_path(app_data, f"app.{source}")

    if value is not None:
        return value

    return resolve_path(app_data, f"var.{source}")


# ---------------------------------------------------------------------------
# Transform pipeline
# ---------------------------------------------------------------------------

def apply_transforms(value, transforms):
    """Apply a list of transform steps to a value.

    Supported types: replace, join, split, lower, upper, title, trim,
    url_encode, regex_replace, prefix, suffix, default, sort, unique.
    """

    if not transforms:
        return value

    for step in transforms:

        t = step.get("type", "")

        if t == "replace":
            if value is None:
                value = ""
            value = str(value).replace(
                str(step.get("from", "")),
                str(step.get("to", ""))
            )

        elif t == "join":
            if isinstance(value, list):
                value = str(step.get("separator", ", ")).join(str(v) for v in value)
            elif value is None:
                value = ""
            else:
                value = str(value)

        elif t == "split":
            value = str(value or "").split(str(step.get("separator", ",")))

        elif t == "lower":
            value = str(value or "").lower()

        elif t == "upper":
            value = str(value or "").upper()

        elif t == "title":
            value = str(value or "").title()

        elif t == "trim":
            value = str(value or "").strip()

        elif t == "url_encode":
            if isinstance(value, list):
                value = ",".join(str(v) for v in value)
            value = quote(str(value or ""), safe="")

        elif t == "regex_replace":
            value = re.sub(
                str(step.get("pattern", "")),
                str(step.get("replacement", "")),
                str(value or "")
            )

        elif t == "prefix":
            value = str(step.get("value", "")) + str(value or "")

        elif t == "suffix":
            value = str(value or "") + str(step.get("value", ""))

        elif t == "default":
            if value in (None, "", [], {}):
                value = step.get("value", "")

        elif t == "sort":
            if isinstance(value, list):
                value = sorted(str(v) for v in value)

        elif t == "unique":
            if isinstance(value, list):
                seen = set()
                result = []
                for v in value:
                    if v not in seen:
                        seen.add(v)
                        result.append(v)
                value = result

    return value


# ---------------------------------------------------------------------------
# Encoding helpers
# ---------------------------------------------------------------------------

def encode_shields(text, replacements=None):
    """Encode a badge text value for shields.io URLs.

    Pass None to apply DEFAULT_REPLACEMENTS (old behavior, no transforms).
    Pass {} to skip string replacements (use when transforms already handled them).
    """

    if text is None:
        text = ""

    text = str(text)

    if replacements is None:
        replacements = DEFAULT_REPLACEMENTS

    for old, new in replacements.items():
        text = text.replace(old, new)

    return quote(text, safe="")


def apply_case(value, uppercase=False, lowercase=False):

    value = str(value)

    if uppercase:
        value = value.upper()

    if lowercase:
        value = value.lower()

    return value


def apply_template(value, prefix="", suffix="", template="{prefix}{value}{suffix}"):

    return template.format(prefix=prefix, value=value, suffix=suffix)


def build_query(query, replacements=None):

    if not query:
        return ""

    encoded = {}

    for key, value in query.items():

        if isinstance(value, list):
            encoded[key] = value
        else:
            encoded[key] = encode_shields(value, replacements)

    return urlencode(encoded, doseq=True)


def build_badge_url(
        label,
        value,
        color="blue",
        style="flat-square",
        logo=None,
        logo_color=None,
        logo_url=None,
        query=None,
        replacements=None):

    label_enc = encode_shields(label, replacements)
    value_enc = encode_shields(value, replacements)
    color_enc = encode_shields(color, replacements)

    params = {"style": style}

    if logo:
        params["logo"] = logo

    if logo_color:
        params["logoColor"] = logo_color

    if logo_url:
        params["logoUrl"] = logo_url

    if query:
        params.update(query)

    query_string = build_query(params, replacements)

    return (
        f"https://img.shields.io/badge/{label_enc}-{value_enc}-{color_enc}"
        f"?{query_string}"
    )


def render_variables(text, variables, replacements=None):

    if text is None:
        return ""

    for key, value in variables.items():
        text = text.replace(
            "{" + key + "}",
            encode_shields(str(value), replacements)
        )

    return text


def build_custom_shield(shield, variables, replacements=None):

    return render_variables(shield, variables, replacements)


def render_markdown(label, url, target_url=None):

    badge = f"![{label}]({url})"

    if target_url:
        return f"[{badge}]({target_url})"

    return badge
