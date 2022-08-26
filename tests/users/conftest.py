# Описываем фикстуры для тестирования
import pytest
import requests
from configuration import SERVICE_URL_2


# scope='function' - по умолчанию - фикстура выполняется каждый тест кейс
# scope='session' - фикстура выполняется только 1 раз (удобно, когда надо логиться админом, коннектиться к БД)
# Если autouse=True, фикстуру аргументом передавать не нужно, она выполнится и без этого для каждого теста
# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture()
def get_users():
    response = requests.get(SERVICE_URL_2)
    return response
