""""Storage Client."""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List

from bson.json_util import dumps


class StorageClient:
    """Store The System Output."""

    def __init__(self):
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def save_json_file(self, file_path: Path, data: List[Dict[str, str]]) -> None:
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            self.__logger.info(f"Saved data to {file_path}")
        except Exception as e:
            self.__logger.error(f"Failed to save data to {file_path}: {e}")
            raise e
