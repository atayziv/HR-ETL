import logging

from fastapi_server.clients.examples_client import ExamplesClient
from fastapi_server.data_models.example import ExampleRequest, ExampleResponse


class ExamplesService:
    def __init__(
        self,
        examples_client: ExamplesClient,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__examples_client = examples_client

    def get_extension_response(self, example_request: ExampleRequest) -> ExampleResponse:
        self.__logger.debug("Getting extension response...")
        result = self.__examples_client.get_extension(example_request.path)
        return ExampleResponse(
            path=example_request.path,
            extension=result,
        )
