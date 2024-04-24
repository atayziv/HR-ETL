from pydantic import Field

from hr_etl.data_models.base import SharedBaseModel


class InfoResponse(SharedBaseModel):
    api: str = Field(description="api name")
    version: str = Field(description="api version")
