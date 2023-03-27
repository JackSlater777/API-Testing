import json
import pytest
import requests
from wiremock.client import *
from microservices.configuration import BODIES_PATH, URL_V2, WIREMOCK_HOST
from microservices.env_vars.clone import SSO_URL
from microservices.mappings import local, proxying_to_google, vasp_checkpartner_417

# pytest microservices/tests/test_microservice.py -s -v


class TestItemTypeMicroservice:
    """Тестируем какой-нибудь тест сьют."""

    @pytest.mark.skip
    def test_local(self, get_wiremock_server_session):
        """Тестируем тест кейс c локальным маппингом."""
        Mappings.create_mapping(mapping=local)  # Создаем мок
        response = requests.get(f'{WIREMOCK_HOST}/hello')  # Делаем запрос
        print(f'\n{response}')  # <Response [407]>
        print(response.text)  # Nobody is at home!

    @pytest.mark.skip
    def test_proxying_to_google(self, get_wiremock_server_session):
        """Тестируем тест кейс c переадресованием на google.com."""
        Mappings.create_mapping(mapping=proxying_to_google)  # Создаем мок
        response = requests.get(f'{WIREMOCK_HOST}/services')  # Делаем запрос
        print(f'\n{response}')  # <Response [200]>
        print(response.text)  # Код страницы

    @pytest.mark.skip
    def test_get_417_from_vasp_v2(self, get_wiremock_server_session):
        """Тест кейс c 407 ошибкой от VASP."""
        Mappings.create_mapping(mapping=vasp_checkpartner_417)  # Создаем мок
        with open(f'{BODIES_PATH}/vasp_checkpartner_417.json', "r") as read_file:  # Подгружаем тело запроса из json'a
            body = json.load(read_file)
        login = 'MGF_EAPI'
        appl_code = 'MGF_EAPI_APPL'
        response = requests.post(f'{SSO_URL}{URL_V2}/?LOGIN={login}&APPL_CODE={appl_code}', json=body)
        assert response.status_code == 200
        assert response.json()['result']['result_check_sync']['isAvailable'] is False
        assert response.json()['result']['result_check_sync']['productOfferingPrice']['productStatus'] == "ACTIVE_TRIAL"


if __name__ == '__main__':
    pytest.main()
