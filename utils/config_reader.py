from pathlib import Path

import yaml


class ConfigReader:
    CONFIG_PATH = Path(__file__).parent.parent / "config" / "settings.yaml"

    @staticmethod
    def load_config() -> dict:
        try:
            with open(ConfigReader.CONFIG_PATH, "r") as f:
                return yaml.safe_load(f)
        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"Config loading error: {e}")
            return None

    @staticmethod
    def get(key: str, default=None):
        config = ConfigReader.load_config()
        if not config:
            return default

        keys = key.split(".")
        value = config
        for k in keys:
            value = value.get(k, default)
            if value is None:
                return default
        return value
