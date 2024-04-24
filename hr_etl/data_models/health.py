from hr_etl.data_models.base import SharedBaseModel


class HealthResponse(SharedBaseModel):
    status: str = "OK"
