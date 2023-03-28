import pytest
# import time
# import requests
# from wiremock.client import *
from wiremock.server import WireMockServer
from wiremock.constants import Config
# from microservices.resource import get_auth_string
from microservices.configuration import LOCAL_WIREMOCK_HOST, LOCAL_WIREMOCK_PORT


@pytest.fixture(scope="session")
def get_local_wiremock_server():
    """Фикстура для создания и запуска локального сервера wiremock с маппингом."""
    wm = WireMockServer()
    wm.port = LOCAL_WIREMOCK_PORT
    Config.base_url = f'{LOCAL_WIREMOCK_HOST}/__admin'
    try:
        wm.start()  # Поднимаем сервер
        # Mappings.delete_all_mappings()  # Удаляем на сервере все моки
        yield wm
    finally:
        # requests.post(f'{Config.base_url}/mappings/save')  # Сохраняем все моки в json-файлы в папке mappings
        # time.sleep(15)
        wm.stop()  # Отключаем сервер


###############################################################################
@pytest.fixture(scope="session")
def suite_setup():
    pass
