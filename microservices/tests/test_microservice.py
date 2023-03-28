import json
import pytest
import requests
from wiremock.client import *
from microservices.configuration import BODIES_PATH, URL, URL_V2, LOCAL_WIREMOCK_HOST, LOGIN, APPL_CODE
from microservices.env_vars.clone import SSO_URL
from microservices.mappings import local, proxying_to_google, vasp_checkpartner_417, vasp_act
from microservices.resource import delete_mapping_by_scenario_name, create_connection_to_rabbitmq_in_clone

# pytest microservices/tests/test_microservice.py -s -v


class TestItemTypeMicroservice:
    """Тестируем какой-нибудь тест сьют."""

    # @pytest.mark.skip
    def test_local(self, get_local_wiremock_server):
        """Тестируем тест кейс c локальным маппингом."""
        Mappings.create_mapping(mapping=local)  # Создаем мок
        response = requests.get(f'{LOCAL_WIREMOCK_HOST}/hello')  # Делаем запрос
        # print(f'\n{response}')  # <Response [407]>
        # print(response.text)  # Nobody is at home!
        assert response.status_code == 407
        assert response.text == 'Nobody is at home!'
        delete_mapping_by_scenario_name(local.get_json_data()['scenarioName'], LOCAL_WIREMOCK_HOST)  # Удаляем мок

    @pytest.mark.skip
    def test_proxying_to_google(self, get_local_wiremock_server):
        """Тестируем тест кейс c переадресованием на google.com."""
        Mappings.create_mapping(mapping=proxying_to_google)  # Создаем мок
        response = requests.get(f'{LOCAL_WIREMOCK_HOST}/services')  # Делаем запрос
        # print(f'\n{response}')  # <Response [200]>
        # print(response.text)  # Код страницы
        assert response.status_code == 200
        delete_mapping_by_scenario_name(proxying_to_google.get_json_data()['scenarioName'], LOCAL_WIREMOCK_HOST)  # Удаляем мок

    @pytest.mark.skip
    def test_uc07_5_get_417_from_vasp_v2(self, get_local_wiremock_server):
        """Тест кейс c 407 ошибкой от VASP."""
        Mappings.create_mapping(mapping=vasp_checkpartner_417)  # Создаем мок
        with open(f'{BODIES_PATH}/vasp_checkpartner_417.json', "r") as read_file:  # Подгружаем тело запроса из json'a
            body = json.load(read_file)
        response = requests.post(f'{SSO_URL}{URL_V2}/?LOGIN={LOGIN}&APPL_CODE={APPL_CODE}', json=body)
        assert response.status_code == 200
        assert response.json()['result']['result_check_sync']['isAvailable'] is False
        assert response.json()['result']['result_check_sync']['productOfferingPrice']['productStatus'] == "ACTIVE_TRIAL"
        delete_mapping_by_scenario_name(vasp_checkpartner_417.get_json_data()['scenarioName'], LOCAL_WIREMOCK_HOST)  # Удаляем мок

    @pytest.mark.skip
    def test_uc01_1_activation_subscription(self, get_local_wiremock_server):
        """Тест кейс c 407 ошибкой от VASP."""
        # Пурджим очереди
        #

        Mappings.create_mapping(mapping=vasp_act)  # Создаем мок
        with open(f'{BODIES_PATH}/vasp_act.json', "r") as read_file:  # Подгружаем тело запроса из json'a
            body = json.load(read_file)
        response = requests.post(f'{SSO_URL}{URL}/?LOGIN={LOGIN}&APPL_CODE={APPL_CODE}', json=body)
        assert response.status_code == 200
        create_connection_to_rabbitmq_in_clone()  # Установливаем соединения с внутренней очередью RabbitMQ

        # In progress

        delete_mapping_by_scenario_name(vasp_act.get_json_data()['scenarioName'], LOCAL_WIREMOCK_HOST)  # Удаляем мок


if __name__ == '__main__':
    pytest.main()
