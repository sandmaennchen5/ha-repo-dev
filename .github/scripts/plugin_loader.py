import importlib


def load_plugin(plugin_name):

    try:
        module = importlib.import_module(f"plugins.{plugin_name}")
        return module.Plugin()
    except (ImportError, AttributeError) as e:
        raise RuntimeError(f"Failed to load plugin '{plugin_name}': {e}") from e
