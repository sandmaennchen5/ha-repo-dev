from common import (
    render,
    OUTPUT_DIR
)


def render_matrix(
    config,
    apps
):

    matrix_cfg = config.get(
        "matrix",
        {}
    )

    empty_values = {

        str(v).lower()

        for v in matrix_cfg.get(
            "empty_values",
            []
        )

    }

    badges_list = []

    for app in apps:

        for badge in app["badges"]:

            value = str(
                badge.get(
                    "value",
                    ""
                )
            ).strip().lower()

            if value in empty_values:

                continue

            badges_list.append({
                "app_name": app["name"],
                "app_slug": app["slug"],
                "label": badge["label"],
                "value": badge["value"],
                "group": badge.get("group", ""),
                "url": badge.get("url", ""),
            })

    render(
        "matrix.html",
        OUTPUT_DIR /
        "matrix.html",
        config=config,
        apps=apps,
        badges_list=badges_list
    )