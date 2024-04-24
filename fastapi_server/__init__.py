import os

from fastapi_server.constants import SETTINGS

__all__ = ("SETTINGS",)

os.chdir(SETTINGS.ROOT_DIR)
