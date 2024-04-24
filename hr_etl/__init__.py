import os

from hr_etl.constants import SETTINGS

__all__ = ("SETTINGS",)

os.chdir(SETTINGS.ROOT_DIR)
