from plugins.base import BadgePlugin


class Plugin(BadgePlugin):
    """Returns the app version from config.yaml as the upstream release tag."""

    def generate(self, app_data, definition):

        version = app_data["app"].get("version", "unknown")

        return {
            "value": version,
            "color": "green"
        }
