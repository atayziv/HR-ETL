from fastapi_server.data_models.base import SharedBaseModel


class HealthResponse(SharedBaseModel):
    status: str = "OK"
