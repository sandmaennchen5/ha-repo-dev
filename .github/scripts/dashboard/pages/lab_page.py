from common import (
    render,
    OUTPUT_DIR
)


def render_lab(
        config):

    render(
        "lab.html",
        OUTPUT_DIR /
        "lab.html",
        config=config
    )