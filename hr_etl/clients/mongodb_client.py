"""MongoDB client."""

import logging
from typing import Dict, List

from pymongo import MongoClient


class MongoDBClient:
    def __init__(self, connection_string: str, db_name: str) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__connection_string = connection_string
        self.__db_name = db_name

    def load_data_to_mongo(self, transformed_data: List[Dict[str, str]]):
        self.__logger.debug(
            "Inserting Transfomed Data Into MongoDB 'employees' Collection"
        )
        client = MongoClient(self.__connection_string)
        db = client[self.__db_name]
        employees_collection = db["employees"]
        employees_collection.create_index([("employee_id", 1)], unique=True)
        employees_collection.insert_many(transformed_data)
