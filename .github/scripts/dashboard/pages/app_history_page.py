from common import (
    render,
    OUTPUT_DIR
)


def render_app_history_pages(
        config,
        apps,
        history):

    for app in apps:

        app_history = []

        for snapshot in history:

            for hist_app in snapshot["apps"]:

                if hist_app["slug"] == app["slug"]:

                    app_history.append({

                        "timestamp":
                            snapshot["timestamp"],

                        "score":
                            hist_app["score"],

                        "green":
                            hist_app["green"],

                        "yellow":
                            hist_app["yellow"],

                        "red":
                            hist_app["red"],

                        "badges":
                            hist_app["badges"]

                    })

        render(

            "app_history.html",

            OUTPUT_DIR
            / "apps"
            / app["slug"]
            / "history.html",

            config=config,

            app=app,

            history=app_history

        )