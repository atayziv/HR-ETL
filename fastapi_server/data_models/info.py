from pydantic import Field

from fastapi_server.data_models.base import SharedBaseModel


class InfoResponse(SharedBaseModel):
    api: str = Field(description="api name")
    version: str = Field(description="api version")
