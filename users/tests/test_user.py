import pytest
from users.src.schemas.user import User
from pydantic import ValidationError
from users.tests.mocks import mock_user, validated_mock_user, invalid_mock_user


class TestUsers:
    def test_status_code(self, get_data_from_response):
        """Проверяем статус-код."""
        get_data_from_response.assert_status_code(200)

    def test_response_validation(self, get_data_from_response):
        """Проверяем валидацию запроса."""
        get_data_from_response.validate(User)  # Валидируем объект
        print(get_data_from_response.get_parsed_item())  # Смотрим результат

    def test_json_validation(self, get_data_from_json):
        """Проверяем валидацию json'a."""
        get_data_from_json.validate(User)  # Валидируем объект
        print(get_data_from_json.get_parsed_item())  # Смотрим результат

    def test_user_count(self, get_data_from_response):
        """Проверяем длину словаря с данными."""
        assert len(get_data_from_response.data) == 10

    @pytest.mark.skip('[ISSUE-2341]')
    def test_mock_user_validation_positive(self):
        """Позитивный тест валидации mock-объекта."""
        assert User.parse_obj(mock_user) == validated_mock_user

    @pytest.mark.development
    def test_mock_user_validation_negative(self):
        """Негативный тест валидации mock-объекта с некорректным значением почты."""
        with pytest.raises(ValidationError):
            User.parse_obj(invalid_mock_user)


if __name__ == '__main__':
    pytest.main()
