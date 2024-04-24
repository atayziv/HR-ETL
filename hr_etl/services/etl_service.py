import logging

from hr_etl.clients.reader_client import ReaderClient
from hr_etl.data_models.example import ExampleRequest, ExampleResponse


class ETLService:
    def __init__(
        self,
        reader_client: ReaderClient,
        json_input_path: str,
    ) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.__reader_client = reader_client
        self.__json_input_path = json_input_path

    def extraction(self) -> None:
        self.__logger.debug("Handle Json File...")
        data = self.__reader_client(self.__json_input_path)
        for employee_data in data:
            
