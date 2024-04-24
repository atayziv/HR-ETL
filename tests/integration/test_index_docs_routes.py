import requests
from fastapi import status

from fastapi_server import SETTINGS
from fastapi_server.data_models.info import InfoResponse


def test_index(fastapi_server_base_url: str) -> None:
    # Act
    response = requests.get(
        url=fastapi_server_base_url,
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK

    actual = response.json()
    expected = InfoResponse(api=SETTINGS.NAME, version=SETTINGS.VERSION)
    assert actual == expected


def test_docs_request(fastapi_server_base_url: str) -> None:
    # Act
    response = requests.get(
        url=f"{fastapi_server_base_url}/docs",
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK


def test_redoc_request(fastapi_server_base_url: str) -> None:
    # Act
    response = requests.get(
        url=f"{fastapi_server_base_url}/redoc",
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK
