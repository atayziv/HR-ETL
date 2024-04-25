import json
import logging
import os
from datetime import datetime
from typing import Dict

from hr_etl.clients.extractor_client import ReaderClient
from hr_etl.clients.mongodb_client import MongoDBClient


class ETLService:
    def __init__(
        self,
        reader_client: ReaderClient,
        mongo_client: MongoDBClient,
        json_file_path: str,
        employees_over_30_json_path: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__employees_over_30_json_path = employees_over_30_json_path
        self.__reader_client = reader_client
        self.__mongo_client = mongo_client
        self.__result_json_data = []
        self.__unique_ids = set()
        self.etl(json_file_path)

    def etl(self, json_file_path: str) -> None:
        self.__logger.debug(
            f"Extract Data From Input Json File: {os.path.basename(json_file_path)}"
        )
        try:
            data = self.__reader_client.extract_data(json_file_path)
            for employee_data in data:
                employee_tranformed_data = self.transformation(employee_data)
                if employee_tranformed_data is not None:
                    self.__result_json_data.append(employee_tranformed_data)
            try:
                self.__mongo_client.load_data_to_mongo(self.__result_json_data)
            except Exception as e:
                self.__logger.error(
                    f"An error occurred while inserting data into MongoDB: {e}"
                )
                raise
            self.__mongo_client.query_mongo(self.__employees_over_30_json_path)
        except json.JSONDecodeError as error:
            self.__logger.exception(error)
            raise

    def transformation(self, employee_data: Dict[str, str]) -> Dict[str, str]:
        employee_id = employee_data["employee_id"]
        if (
            employee_id not in self.__unique_ids
            and employee_data["department"] != "Unknown"
        ):
            self.__logger.debug(f"Strat tanformation on employee: {employee_id}")
            self.__unique_ids.add(employee_id)
            full_name = employee_data["first_name"] + " " + employee_data["last_name"]
            age = (
                datetime.today().year
                - datetime.strptime(employee_data["date_of_birth"], "%Y-%m-%d").year
            )
            salary = int(employee_data["salary"])
            return {
                "employee_id": employee_id,
                "first_name": employee_data["first_name"],
                "last_name": employee_data["last_name"],
                "full_name": full_name,
                "department": employee_data["department"],
                "position": employee_data["position"],
                "salary": salary,
                "date_of_birth": employee_data["date_of_birth"],
                "age": age,
            }
