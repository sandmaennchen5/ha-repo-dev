from common import (
    render,
    OUTPUT_DIR
)


def render_index(
        config,
        apps,
        stats):

    render(
        "index.html",
        OUTPUT_DIR /
        "index.html",
        config=config,
        apps=apps,
        stats=stats
    )