import pytest

from hr_etl.clients.reader_client import ExamplesClient


@pytest.fixture(scope="session")
def examples_client() -> ExamplesClient:
    return ExamplesClient()
