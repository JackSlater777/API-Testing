import pytest
import json
from computers.configuration import JSON_PATH
from computers.src.baseclasses.object_validator import ObjectValidator


@pytest.fixture
def get_data_from_json():
    """Фикстура для декодирования json-файла в python объект."""
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        data = json.load(read_file)
    obj = ObjectValidator(data)  # Скармливаем объект в класс
    return obj  # Возвращаем объект в тест
