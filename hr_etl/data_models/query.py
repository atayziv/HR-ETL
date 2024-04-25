from typing import Any, Dict

from hr_etl.data_models.base import SharedBaseModel


class QueryStructure(SharedBaseModel):
    query: Dict[str, Dict[str, Any]]
