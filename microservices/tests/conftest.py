import pytest
from wiremock.server import WireMockServer
from wiremock.constants import Config
from microservices.configuration import LOCAL_WIREMOCK_URL, LOCAL_WIREMOCK_PORT, WIREMOCK_URL, WIREMOCK_PORT


@pytest.fixture(scope="session")
def get_local_wiremock_server():
    """Фикстура для создания и запуска локального сервера wiremock с маппингом."""
    wm = WireMockServer()
    wm.port = LOCAL_WIREMOCK_PORT
    Config.base_url = f'{LOCAL_WIREMOCK_URL}/__admin'
    try:
        wm.start()  # Поднимаем сервер
        yield wm
    finally:
        wm.stop()  # Отключаем сервер


@pytest.fixture(scope="session")
def get_clone_wiremock_server():
    """Фикстура для коннекта с сервером wiremock на клоне."""
    wm = WireMockServer()
    wm.port = WIREMOCK_PORT
    Config.base_url = f'{WIREMOCK_URL}/__admin'
    yield wm
