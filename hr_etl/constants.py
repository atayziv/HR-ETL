import os


def get_from_env(key: str, default_value: str) -> str:
    return str(os.getenv(key)) if key in os.environ else default_value


class SETTINGS:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG = get_from_env("CONFIG", os.path.join(ROOT_DIR, "config.yaml"))
    NAME = "ETL SERVICE"
    VERSION = "0.1.0"
    ETL_MONGODB_ALIAS = "employees"

