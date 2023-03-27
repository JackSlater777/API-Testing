import pytest
# import time
# import requests
# from wiremock.client import *
from wiremock.server import WireMockServer
from wiremock.constants import Config
from microservices.configuration import WIREMOCK_HOST, WIREMOCK_PORT


@pytest.fixture(scope="session")
def get_wiremock_server_session():
    """Фикстура для создания и запуска локального сервера wiremock с маппингом."""
    wm = WireMockServer()
    wm.port = WIREMOCK_PORT
    Config.base_url = f'{WIREMOCK_HOST}/__admin'
    try:
        wm.start()  # Поднимаем сервер
        # Mappings.delete_all_mappings()  # Удаляем на сервере все моки
        yield wm
    finally:
        # requests.post(f'{Config.base_url}/mappings/save')  # Сохраняем все моки в json-файлы в папке mappings
        # time.sleep(15)
        wm.stop()  # Отключаем сервер
