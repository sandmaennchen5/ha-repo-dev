from common import render, OUTPUT_DIR

def render_badges(config, badges):
    render(
        "badges.html",
        OUTPUT_DIR / "badges.html",
        config=config,
        badges=badges
    )
