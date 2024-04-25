from typing import Any, Dict

from hr_etl.data_models.base import SharedBaseModel


class Query(SharedBaseModel):
    operator: str
    value: Any


class QueryStructure(SharedBaseModel):
    query: Dict[str, Dict[str, Any]]
