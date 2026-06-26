from common import (
    render,
    OUTPUT_DIR
)


def render_app_pages(
        config,
        apps):

    for app in apps:

        app_dir = (
            OUTPUT_DIR /
            "apps" /
            app["slug"]
        )

        render(
            "app.html",
            app_dir /
            "index.html",
            config=config,
            app=app
        )