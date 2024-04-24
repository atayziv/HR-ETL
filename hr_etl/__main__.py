import logging

from dependency_injector.wiring import inject

from hr_etl.constants import SETTINGS
from hr_etl.containers import Container


@inject
def init() -> None:
    container = Container()
    container.config.from_yaml(SETTINGS.CONFIG)
    container.init_resources()
    logger = logging.getLogger(__name__)
    logger.info(f"Welcome to {SETTINGS.NAME}")
    container.etl_service()


if __name__ == "__main__":
    init()
