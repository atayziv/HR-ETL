"""MongoDB client."""

import logging
from typing import Dict, List

from bson.json_util import dumps
from pymongo import MongoClient

from hr_etl.clients.storage_client import StorageClient


class MongoDBClient:
    """MongoDB Client Class."""

    def __init__(
        self,
        storage_client: StorageClient,
        connection_string: str,
        db_name: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__storage_client = storage_client
        self.__client = MongoClient(connection_string)
        self.__employees_collection = self.__client[db_name]["employees"]

    def load_data_to_mongo(self, transformed_data: List[Dict[str, str]]):
        self.__logger.debug(
            "Inserting Transfomed Data Into MongoDB 'employees' Collection"
        )
        self.__employees_collection.create_index("employee_id", unique=True)
        self.__employees_collection.insert_many(transformed_data)

    def query_mongo(self, output_path: str):
        self.__logger.debug("Query Mongo to return all employees over the age of 30")
        query = {"age": {"$gt": 30}}
        results = self.__employees_collection.find(query)
        json_data = dumps(results)
        self.__storage_client.save_json_file(output_path, json_data)
