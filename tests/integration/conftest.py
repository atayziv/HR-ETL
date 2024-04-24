import os
from typing import Any, List, Tuple

import pytest


def start_docker(docker_services: Any, docker_name: str, port: int) -> Tuple[str, str]:
    docker_services.start(docker_name)
    public_port = docker_services.wait_for_service(docker_name, port)
    return docker_services.docker_ip, str(public_port)


@pytest.fixture(scope="session")
def integration_tests_folder() -> str:
    return os.path.dirname(__file__)


@pytest.fixture(scope="session")
def docker_compose_files(pytestconfig: Any, integration_tests_folder: str) -> List[str]:
    return [os.path.join(integration_tests_folder, "docker-compose.yml")]


@pytest.fixture(scope="session")
def fastapi_server_base_url(docker_services: Any) -> str:
    host, port = start_docker(docker_services, "fastapi-server", 5000)
    return f"http://{host}:{port}"
