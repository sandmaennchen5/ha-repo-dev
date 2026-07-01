from pathlib import Path
import json
import shutil

from jinja2 import Environment, FileSystemLoader

from utils import load_config_sections

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = Path(".dashboard")
TEMPLATE_DIR = BASE_DIR / "templates"
ASSET_DIR = BASE_DIR / "assets"


def load_dashboard_config():
    _, dashboard_data = load_config_sections()
    return dashboard_data


def get_environment():

    return Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def ensure_dirs():

    for sub in ("apps", "assets", "data", "badges"):
        (OUTPUT_DIR / sub).mkdir(parents=True, exist_ok=True)


def copy_assets():

    if not ASSET_DIR.exists():
        return

    for file in ASSET_DIR.iterdir():

        if file.is_file():
            shutil.copy2(file, OUTPUT_DIR / "assets" / file.name)


def export_json(filename, data):

    with open(OUTPUT_DIR / "data" / filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def render(template_name, target, **kwargs):

    env = get_environment()
    template = env.get_template(template_name)
    config = load_dashboard_config()

    site = config.get("site", {})
    theme = config.get("theme", {})
    base_url = site.get("base_url", "")
    asset_path = site.get("asset_path", "assets")

    kwargs.pop("config", None)

    context = {
        "config": config,
        "site": site,
        "theme": theme,
        "base_url": base_url,
        "asset_path": asset_path,
    }

    context.update(kwargs)

    html = template.render(**context)

    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w", encoding="utf-8") as f:
        f.write(html)
