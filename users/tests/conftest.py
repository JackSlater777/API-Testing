import pytest
import json
import requests
from unittest.mock import patch, MagicMock
from users.configuration import JSON_PATH
from users.src.baseclasses.response_validator import ResponseValidator
from users.src.baseclasses.object_validator import ObjectValidator
from users.configuration import SERVICE_URL


# # # Фикстуры для классических тестов
@pytest.fixture
def response():
    """Фикстура для формирования экземпляра ответа."""
    r = requests.get(SERVICE_URL)
    return r


@pytest.fixture
def decode_json():
    """Фикстура для декодирования json-файла в python объект."""
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        full_data = json.load(read_file)
    data = full_data.get("data")  # Конкретизируем данные под валидацию если необходимо - только data
    return data


# # # Фикстуры для тестов с классами
@pytest.fixture
def get_data_from_response(response):
    """Фикстура для прогона ответа через класс."""
    data = response.json().get("data")  # Конкретизируем данные под валидацию если необходимо - только data
    obj = ResponseValidator(response, data)  # Скармливаем объект в класс
    return obj  # Возвращаем объект в тест


@pytest.fixture
def get_data_from_json(decode_json):
    """Фикстура для прогона объекта через класс."""
    obj = ObjectValidator(decode_json)  # Скармливаем объект в класс
    return obj  # Возвращаем объект в тест


# # # Фикстуры для тестов с моками
@pytest.fixture
@patch("users.tests.conftest.requests")
def positive_response_mocker(requests_mock, decode_json):
    """Фикстура для формирования mock-ответа для позитивного тестирования."""
    response_mock = MagicMock()  # Заменяем response mock-объектом
    response_mock.status_code = 200  # Задаем атрибут status_code и значение, которое он имеет
    response_mock.json.return_value = decode_json  # Задаем метод json и значение, которое он возвращает
    requests_mock.get.return_value = response_mock  # Теперь запрос будет возвращать mock-объект с заданным поведением
    return requests_mock


@pytest.fixture
@patch("users.tests.conftest.requests")
def negative_response_mocker(requests_mock, set_invalid_email):
    """Фикстура для формирования mock-ответа для негативного тестирования."""
    response_mock = MagicMock()
    response_mock.status_code = 404
    response_mock.json.return_value = set_invalid_email
    requests_mock.get.return_value = response_mock
    return requests_mock


@pytest.fixture
def set_invalid_email(decode_json):
    """Функция для изменения значения email в json'e на невалидный."""
    for user in decode_json:
        user["email"] = "faked_email"
    return decode_json
