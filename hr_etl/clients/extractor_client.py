""""Extractor Client."""

import json
from typing import Any


class ExtractorClient:
    """Extract data from Json File Client."""

    def extract_employees_data(self, json_path: str) -> Any:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
