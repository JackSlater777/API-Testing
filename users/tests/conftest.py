import pytest
import json
import requests
from users.configuration import JSON_PATH
from users.src.baseclasses.response_validator import ResponseValidator
from users.src.baseclasses.object_validator import ObjectValidator
from users.configuration import SERVICE_URL


@pytest.fixture
def get_data_from_response():
    """Фикстура для формирования экземпляра ответа."""
    r = requests.get(SERVICE_URL)  # Делаем запрос
    data = r.json().get("data")  # Конкретизируем данные под валидацию если необходимо - только data
    response = ResponseValidator(r, data)  # Скармливаем ответ в класс
    return response  # Возвращаем объект в тест


@pytest.fixture
def get_data_from_json():
    """Фикстура для декодирования json-файла в python объект."""
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        full_data = json.load(read_file)
    data = full_data.get("data")  # Конкретизируем данные под валидацию если необходимо (только data, без meta)
    obj = ObjectValidator(data)  # Скармливаем объект в класс
    return obj  # Возвращаем объект в тест
