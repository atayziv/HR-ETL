import os


def get_from_env(key: str, default_value: str) -> str:
    return str(os.getenv(key)) if key in os.environ else default_value


class SETTINGS:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG = get_from_env("CONFIG", os.path.join(ROOT_DIR, "config.yaml"))
    NAME = "ETL SERVICE"
    ETL_MONGODB_ALIAS = "employees"


class Constants:
    invalid_department = "Unknown"
