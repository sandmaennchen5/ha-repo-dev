from common import (
    render,
    OUTPUT_DIR
)


def render_apps_index(
        config,
        apps):

    render(
        "apps.html",
        OUTPUT_DIR /
        "apps" /
        "index.html",
        config=config,
        apps=apps
    )