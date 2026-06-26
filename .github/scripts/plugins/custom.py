from plugins.base import BadgePlugin


class Plugin(BadgePlugin):

    def generate(self, app_data, definition):

        return {
            "value": "custom",
            "color": "blue"
        }
