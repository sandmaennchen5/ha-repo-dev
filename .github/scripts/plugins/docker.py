from plugins.base import BadgePlugin


class Plugin(BadgePlugin):
    """Fetches Docker image size (stub – implement as needed)."""

    def generate(self, app_data, definition):

        return {
            "value": "latest",
            "color": "blue"
        }
