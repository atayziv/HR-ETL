import logging.config

from dependency_injector import containers, providers

from hr_etl.clients.extractor_client import ExtractorClient
from hr_etl.clients.mongodb_client import MongoDBClient
from hr_etl.clients.storage_client import StorageClient
from hr_etl.services.etl_service import ETLService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    extractor_client = providers.Singleton(
        ExtractorClient,
    )

    storage_client = providers.Singleton(
        StorageClient,
    )

    mongo_client = providers.Resource(
        MongoDBClient,
        connection_string=config.mongodb.connection_string,
        db_name=config.mongodb.db_name,
    )

    etl_service = providers.Singleton(
        ETLService,
        extractor_client=extractor_client,
        mongo_client=mongo_client,
        storage_client=storage_client,
        input_file_path=config.input_file_path,
        employees_over_30_output_path=config.employees_over_30_output_path,
    )
