import logging.config

from dependency_injector import containers, providers

from hr_etl.clients import mongodb_client
from hr_etl.clients.mongodb_client import MongoDBClient
from hr_etl.clients.reader_client import ReaderClient
from hr_etl.services.etl_service import ETLService

from . import SETTINGS


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    reader_client = providers.Singleton(
        ReaderClient,
    )

    mongo_client = providers.Resource(
        MongoDBClient,
        connection_string=config.mongodb.connection_string,
        db_name=config.mongodb.db_name,
    )

    etl_service = providers.Singleton(
        ETLService,
        reader_client=reader_client,
        mongo_client=mongo_client,
        json_file_path=config.json_file_path,
    )
