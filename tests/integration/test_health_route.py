import requests
from fastapi import status


def test_health(fastapi_server_base_url: str) -> None:
    # Arrange
    url = f"{fastapi_server_base_url}/health"

    # Act
    response = requests.get(url)

    # Assert
    assert response.status_code == status.HTTP_200_OK
