from dependency_injector.wiring import inject
from fastapi import APIRouter

from fastapi_server import SETTINGS
from fastapi_server.data_models.info import InfoResponse

router = APIRouter(
    prefix="",
    tags=["Index"],
)


@router.get(
    path="/",
    response_model=InfoResponse,
)
@inject
def index() -> InfoResponse:
    return InfoResponse(api=SETTINGS.NAME, version=SETTINGS.VERSION)
