from common import (
    render,
    OUTPUT_DIR
)


def render_health(
        config,
        apps,
        stats):

    render(
        "health.html",
        OUTPUT_DIR /
        "health.html",
        config=config,
        apps=apps,
        stats=stats
    )