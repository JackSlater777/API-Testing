import pytest
import requests
from wiremock.client import *
from wiremock.server import WireMockServer
from wiremock.constants import Config
from microservices.configuration import local_server_url, local_port
from microservices.mappings import mapping


@pytest.fixture
def get_wiremock_server_session():
    """Фикстура для создания и запуска локального сервера wiremock с маппингом."""
    wm = WireMockServer()
    wm.port = local_port
    Config.base_url = f'{local_server_url}/__admin'
    try:
        wm.start()  # Server is up
        Mappings.delete_all_mappings()  # Clean up
        Mappings.create_mapping(mapping=mapping)  # Set up stubs
        requests.post(f'{Config.base_url}/mappings/save')  # Save mappings into json file in the mappings folder
        yield wm  # Go to test
    finally:
        wm.stop()  # Server is down
