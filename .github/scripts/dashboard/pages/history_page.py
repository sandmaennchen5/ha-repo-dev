from common import (
    render,
    OUTPUT_DIR
)


def render_history(
        config,
        history):

    render(
        "history.html",
        OUTPUT_DIR /
        "history.html",
        config=config,
        history=history
    )