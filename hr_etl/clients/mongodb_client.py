"""MongoDB client."""

import logging
from typing import Dict, List

from pymongo import MongoClient


class MongoDBClient:
    def __init__(self, connection_string: str, db_name: str) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__connection_string = connection_string
        self.__db_name = db_name
        self.__client = MongoClient(self.__connection_string)
        self.__employees_collection = self.__client[self.__db_name]["employees"]

    def load_data_to_mongo(self, transformed_data: List[Dict[str, str]]):
        self.__logger.debug(
            "Inserting Transfomed Data Into MongoDB 'employees' Collection"
        )
        self.__employees_collection.create_index([("employee_id", 1)], unique=True)
        self.__employees_collection.insert_many(transformed_data)

    def query_mongo(self):
        self.__logger.debug("Query Mongo to return all employees over the age of 30")
        query = {"age": {"$gt": 30}}
        results = self.__employees_collection.find(query)
        print("Employees with age over 30:")
        for record in results:
            print(record)
