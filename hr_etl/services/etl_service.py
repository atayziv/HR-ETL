""""Extract, Transform and Load Service."""

import json
import logging
import os
from datetime import datetime
from typing import Dict

from hr_etl.clients.extractor_client import ExtractorClient
from hr_etl.clients.mongodb_client import MongoDBClient
from hr_etl.clients.storage_client import StorageClient


class ETLService:
    """ETL Class."""

    def __init__(
        self,
        extractor_client: ExtractorClient,
        mongo_client: MongoDBClient,
        storage_client: StorageClient,
        input_file_path: str,
        employees_over_30_output_path: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__extractor_client = extractor_client
        self.__mongo_client = mongo_client
        self.__storage_client = storage_client
        self.__employees_over_30_output_path = employees_over_30_output_path
        self.__result_json_data = []
        self.__unique_ids = set()
        self.run_etl_pipline(input_file_path)

    def run_etl_pipline(self, input_file_path: str) -> None:
        self.__logger.info(
            f"Extract Data From Input Json File: {os.path.basename(input_file_path)}"
        )
        try:
            employees_data = self.__extractor_client.extract_employees_data(
                input_file_path
            )
            for employee in employees_data:
                employee_tranformed_data = self.transform_employee_data(employee)
                if employee_tranformed_data:
                    self.__result_json_data.append(employee_tranformed_data)
            self.__mongo_client.load_data_to_mongo(self.__result_json_data)
            query_results_data = self.__mongo_client.query_employees(
                query={"age": {"$gt": 30}}
            )
            self.__storage_client.save_file(
                self.__employees_over_30_output_path, query_results_data
            )
        except json.JSONDecodeError as error:
            self.__logger.exception("Error parsing JSON data: %s", error)
        except Exception as e:
            self.__logger.error(f"An error occurred while working with MongoDB: {e}")

    def transform_employee_data(self, employee_data: Dict[str, str]) -> Dict[str, str]:
        employee_id = employee_data["employee_id"]
        if (
            employee_id not in self.__unique_ids
            and employee_data["department"] != "Unknown"
        ):
            self.__logger.info(f"Strat transformation on employee: {employee_id}")
            self.__unique_ids.add(employee_id)
            full_name = employee_data["first_name"] + " " + employee_data["last_name"]
            age = (
                datetime.today().year
                - datetime.strptime(employee_data["date_of_birth"], "%Y-%m-%d").year
            )
            salary = int(employee_data["salary"])
            self.__logger.info(
                f"Finished processing transform on employee: {employee_id}"
            )
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
