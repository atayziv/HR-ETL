"""MongoDB client."""

import logging
from typing import List

from mongoengine import connect

from hr_etl.data_models.employee import TransformedEmployee
from hr_etl.data_models.query import QueryStructure


class MongoDBClient:
    """MongoDB Client Class."""

    def __init__(
        self,
        connection_string: str,
        db_name: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        connect(db_name, host=connection_string)

    def load_data_to_mongo(self, transformed_data: List[TransformedEmployee]):
        self.__logger.info(
            "Inserting transformed data into the 'employees' collection in MongoDB."
        )
        TransformedEmployee.objects.insert(transformed_data, load_bulk=False)
        self.__logger.info(
            "Data has been successfully inserted into the 'employees' collection."
        )

    def query_employees(self, query: QueryStructure) -> List[TransformedEmployee]:
        self.__logger.info("Querying MongoDB for all employees over the age of 30.")
        results = TransformedEmployee.objects(__raw__=query.query)
        self.__logger.info("Query completed successfully.")
        return results.to_json()
