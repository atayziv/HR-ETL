import logging


class ExamplesClient:
    def __init__(self) -> None:
        self.__logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    @staticmethod
    def __get_extension(path: str) -> str:
        return path.split(".")[-1]

    def get_extension(self, path: str) -> str:
        self.__logger.debug("Getting extension...")
        return self.__get_extension(path)
