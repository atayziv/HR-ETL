from pydantic import Field

from hr_etl.data_models.base import SharedBaseModel


class ExampleRequest(SharedBaseModel):
    path: str = Field(description="path")


class ExampleResponse(SharedBaseModel):
    path: str = Field(description="path")
    extension: str = Field(description="extension")
