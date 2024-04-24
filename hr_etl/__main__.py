import logging

from hr_etl.constants import SETTINGS
from hr_etl.services import etl_service

def init() -> None:
    logger = logging.getLogger(__name__)
    logger.info(f"Welcome to {SETTINGS.NAME}")
    etl_service()


if __name__ == "__main__":
    init()
