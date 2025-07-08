import yaml


class ConfigReader:

    @staticmethod
    def load_config() -> dict:
        with open("../config/settings.yaml", "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get(key: str, default=None):
        config = ConfigReader.load_config()
        keys = key.split(".")
        value = config
        for k in keys:
            value = value.get(k, default)
            if value is None:
                return default
        return value
