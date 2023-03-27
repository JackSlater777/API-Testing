import requests
from microservices.configuration import WIREMOCK_HOST
from wiremock.client import *


def delete_mapping_by_scenario_name(scenario_name):
    """Удаляем мок по имени."""
    mock_list = requests.get(f'{WIREMOCK_HOST}/__admin/').json()['mappings']
    for mock in mock_list:
        if mock['scenarioName'] == scenario_name:
            Mappings.delete_mapping(mock['id'])
