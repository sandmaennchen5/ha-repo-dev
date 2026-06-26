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

    matrix_badges = []

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

            label = badge["label"]

            if label not in matrix_badges:

                matrix_badges.append(
                    label
                )

    matrix_badges = sorted(
        matrix_badges
    )

    max_badges = matrix_cfg.get(
        "max_badges",
        0
    )

    if max_badges:

        matrix_badges = (
            matrix_badges[:max_badges]
        )

    render(
        "matrix.html",
        OUTPUT_DIR /
        "matrix.html",
        config=config,
        apps=apps,
        matrix_badges=matrix_badges
    )