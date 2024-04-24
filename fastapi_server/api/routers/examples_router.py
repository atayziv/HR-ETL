import logging

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from fastapi_server.containers import Container
from fastapi_server.data_models.example import ExampleRequest, ExampleResponse
from fastapi_server.services.examples_service import ExamplesService

router = APIRouter(
    prefix="/examples",
    tags=["Examples"],
)


@router.post(
    path="/extension",
    response_model=ExampleResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
@inject
def extension(
    example_request: ExampleRequest,
    examples_service: ExamplesService = Depends(Provide[Container.examples_service]),
) -> ExampleResponse:
    logger = logging.getLogger(f"{__name__}.{extension.__name__}")
    try:
        logger.info(f"Trying to get file extension with request=({example_request})...")
        response = examples_service.get_extension_response(example_request)
        logger.info(f"Successfully got file extension with request=({example_request})")
        return response
    except ValueError as error:
        logger.warning(error, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Validation Error"
        ) from error
    except FileNotFoundError as error:
        logger.warning(error, exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found") from error
    except Exception as error:
        logger.exception(error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        ) from error
