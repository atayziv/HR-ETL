import requests
from fastapi import status

from fastapi_server.data_models.example import ExampleResponse


def test_extension(fastapi_server_base_url: str) -> None:
    # Arrange
    path = "file.jpg"

    # Act
    response = requests.post(
        url=f"{fastapi_server_base_url}/examples/extension",
        json={"path": path},
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK

    actual = ExampleResponse(**response.json())
    expected = ExampleResponse(path=path, extension="jpg")
    assert actual == expected
