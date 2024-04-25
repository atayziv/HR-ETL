""""Storage Client."""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List


class StorageClient:
    """Store The System Output."""

    def __init__(self):
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def save_file(self, file_path: Path, data: List[Dict[str, str]]) -> None:
        with open(file_path, "w") as json_file:
            json_file.write(data)
        self.__logger.info(f"Saved data to {file_path}")
