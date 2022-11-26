import pytest
import json
from players.src.builders.player import PlayerBuilder
from players.configuration import JSON_PATH
from players.src.baseclasses.object_validator import ObjectValidator


@pytest.fixture
def get_data_from_json():
    """Фикстура для декодирования json-файла в python объект."""
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        data = json.load(read_file)
    obj = ObjectValidator(data)  # Скармливаем объект в класс
    return obj  # Возвращаем объект в тест


@pytest.fixture
def build_player():
    """Фикстура для генерации объекта из билдера."""
    return PlayerBuilder()  # Возвращаем объект в тест
