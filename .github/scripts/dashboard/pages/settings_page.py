from common import render, OUTPUT_DIR


def render_settings(config):

    render(
        "settings.html",
        OUTPUT_DIR / "settings.html",
        config=config
    )