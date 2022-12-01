import pytest
from computers.src.schemas.computer import Computer  # pydantic схема
from computers.src.baseclasses.object_validator import ObjectValidator


class TestComputersClassic:
    """Классические тесты без прогона объектов через специальные классы."""
    def test_json_validation(self, decode_json):
        """Проверяем валидацию json'a."""
        Computer.parse_obj(decode_json)


class TestComputers:
    """Тесты с прогоном объектов через специальные классы."""
    def test_json_validation(self, decode_json):
        """Проверяем валидацию json'a."""
        obj = ObjectValidator(decode_json)  # Скармливаем объект в класс
        obj.validate(Computer)  # Валидируем объект
        print(obj.get_parsed_item())  # Смотрим результат


if __name__ == '__main__':
    pytest.main()
