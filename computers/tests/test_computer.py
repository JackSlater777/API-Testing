import pytest
from computers.src.schemas.computer import Computer  # pydantic схема


class TestComputer:
    def test_json_validation(self, get_data_from_json):
        """Проверяем валидацию json'a."""
        get_data_from_json.validate(Computer)  # Валидируем объект
        print(get_data_from_json.get_parsed_item())  # Смотрим результат


if __name__ == '__main__':
    pytest.main()
