import pytest
import requests
import time
from microservices.tests.conftest import local_server_url

# pytest microservices/tests/test_microservice.py -s -v


class TestItemTypeMicroservice:
    """Тестируем какой-нибудь тест сьют."""
    def test_200(self, get_wiremock_server_session):
        """Тестируем тест кейс."""
        response = requests.get(f'{local_server_url}/hello')  # Make API calls
        print(f'\n{response}')  # <Response [200]>
        print(response.text)  # hi
        time.sleep(3)


if __name__ == '__main__':
    pytest.main()
