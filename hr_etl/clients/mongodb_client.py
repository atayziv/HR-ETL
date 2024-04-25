"""MongoDB client."""

import logging
from typing import Any, Dict, List

from bson import json_util
from pymongo import MongoClient


class MongoDBClient:
    """MongoDB Client Class."""

    def __init__(
        self,
        connection_string: str,
        db_name: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__client = MongoClient(connection_string)
        self.__employees_collection = self.__client[db_name]["employees"]
        self.__employees_collection.create_index("employee_id", unique=True)

    def load_data_to_mongo(self, transformed_data: List[Dict[str, str]]):
        self.__logger.info(
            "Inserting transformed data into the 'employees' collection in MongoDB."
        )
        self.__employees_collection.insert_many(transformed_data)
        self.__logger.info(
            "Data has been successfully inserted into the 'employees' collection."
        )

    def query_employees(self, query: Dict[str, Dict[str, Any]]) -> List[Dict[str, str]]:
        self.__logger.info("Querying MongoDB for all employees over the age of 30.")
        results = self.__employees_collection.find(query)
        self.__logger.info("Query completed successfully.")
        return json_util.dumps(results)
