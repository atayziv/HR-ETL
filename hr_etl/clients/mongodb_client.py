"""MongoDB client."""

import logging
from typing import Dict, List

from mongoengine import connect, disconnect
from pymongo import MongoClient


class MongoDBClient:
    def __init__(self, connection_string: str, db_name: str, db_alias: str) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__connection_string = connection_string
        self.__db_name = db_name
        self.__db_alias = db_alias
        self.init_mongodb_connection()

    # Function to initialize a connection to MongoDB
    def init_mongodb_connection(self):
        """Initialize MongoDB connection and create a generator for connection management."""
        self.__logger.debug(f"Connecting to MongoDB database '{self.__db_name}'...")
        connection = connect(
            db=self.__db_name,
            alias=self.__db_alias,
            host=self.__connection_string,
            tz_aware=True,
            uuidRepresentation="standard",
        )
        self.__logger.debug("Connection established.")

        yield connection

        self.__logger.debug(
            f"Disconnecting from MongoDB database '{self.__db_name}'..."
        )
        disconnect(alias=self.__db_alias)
        self.__logger.debug("Disconnected.")

    def insert_mongo_data(self, transformed_data: List[Dict[str, str]]):
        with self.init_mongodb_connection():
            client = MongoClient(self.__connection_string)

            # Get the database and collection
            db = client[self.__db_name]
            employees_collection = db["employees"]

            # Ensure an index on employee_id
            employees_collection.create_index([("employee_id", 1)], unique=True)

            # Insert the transformed data
            employees_collection.insert_many(transformed_data)
