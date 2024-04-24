""""Reader Client."""

import json
from typing import Any


class ReaderClient:  # pylint: disable=too-few-public-methods
    """Reade Json Files Client."""

    def _read_data(self, json_path: str) -> Any:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
