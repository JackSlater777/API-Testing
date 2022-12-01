import pytest
import json
from computers.configuration import JSON_PATH


@pytest.fixture
def decode_json():
    """Фикстура для декодирования json-файла в python объект."""
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        return json.load(read_file)
