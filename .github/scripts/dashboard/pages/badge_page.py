from common import (
    render,
    OUTPUT_DIR
)


def render_badge_pages(
        config,
        apps):

    for app in apps:

        for badge in app["badges"]:

            render(
                "badge.html",
                OUTPUT_DIR /
                "apps" /
                app["slug"] /
                "badges" /
                f"{badge['id']}.html",
                config=config,
                app=app,
                badge=badge
            )