import requests
import pika
import base64
from wiremock.client import *
from microservices.env_vars.clone import RMQ_IN_HOST, RMQ_IN_HTTP_PORT


def get_auth_string(basic_auth_username, basic_auth_password):
    """Получение строки base64 для авторизации в административном интерфейсе SSO."""
    auth_string = f'{basic_auth_username}:{basic_auth_password}'
    base64_string = base64.encodebytes(auth_string.encode('utf-8')).replace(b'\n', b'')
    return f'Basic {base64_string.decode("utf-8")}'


def create_connection_to_rabbitmq_in_clone():
    """Установливаем соединения с внутренней очередью RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


def delete_mapping_by_scenario_name(scenario_name, wiremock_host):
    """Удаляем мок по имени."""
    mock_list = requests.get(f'{wiremock_host}/__admin/').json()['mappings']
    for mock in mock_list:
        if mock.get('scenarioName') == scenario_name:
            Mappings.delete_mapping(mock['id'])


def purge_queue(queue_name):
    """Очищаем очередь RabbitMQ перед тестом."""
    vhost = 'mfactory'
    requests.delete(f'http://{RMQ_IN_HOST}:{RMQ_IN_HTTP_PORT}/api/queues/{vhost}/{queue_name}/contents')
