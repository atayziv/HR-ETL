import logging.config

from dependency_injector import containers, providers

from hr_etl.clients.extractor_client import ReaderClient
from hr_etl.clients.mongodb_client import MongoDBClient
from hr_etl.clients.storage_client import StorageClient
from hr_etl.services.etl_service import ETLService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    reader_client = providers.Singleton(
        ReaderClient,
    )

    storage_client = providers.Singleton(
        StorageClient,
    )

    mongo_client = providers.Resource(
        MongoDBClient,
        storage_client=storage_client,
        connection_string=config.mongodb.connection_string,
        db_name=config.mongodb.db_name,
    )

    etl_service = providers.Singleton(
        ETLService,
        reader_client=reader_client,
        mongo_client=mongo_client,
        json_file_path=config.json_file_path,
        employees_over_30_json_path=config.employees_over_30_json_path,
    )
