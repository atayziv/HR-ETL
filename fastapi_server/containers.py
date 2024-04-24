import logging.config

from dependency_injector import containers, providers

from fastapi_server.clients.examples_client import ExamplesClient
from fastapi_server.services.examples_service import ExamplesService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    examples_client = providers.Singleton(
        ExamplesClient,
    )

    examples_service = providers.Singleton(
        ExamplesService,
        examples_client=examples_client,
    )
