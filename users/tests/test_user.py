import pytest
from users.src.schemas.user import User
from pydantic import ValidationError


class TestUsersClassic:
    """Классические тесты без прогона объектов через специальные классы."""
    def test_status_code(self, response):
        """Проверяем статус-код."""
        assert response.status_code == 200

    def test_response_validation(self, response):
        """Парсим и валидируем запрос."""
        for user in response.json().get("data"):
            User.parse_obj(user)

    def test_json_validation(self, decode_json):
        """Парсим и валидируем json."""
        for user in decode_json:
            User.parse_obj(user)

    def test_user_count_from_response(self, response):
        """Проверяем длину словаря с данными, полученного с запроса."""
        assert len(response.json().get("data")) == 10

    def test_user_count_from_json(self, decode_json):
        """Проверяем длину словаря с данными, полученного с json'a."""
        assert len(decode_json) == 10


class TestUsers:
    """Тесты с прогоном объектов через специальные классы."""
    @pytest.mark.development
    def test_status_code(self, get_data_from_response):
        """Проверяем статус-код."""
        get_data_from_response.assert_status_code(200)

    @pytest.mark.production
    def test_response_validation(self, get_data_from_response):
        """Парсим и валидируем запрос."""
        get_data_from_response.validate(User)  # Валидируем объект
        print(get_data_from_response.get_parsed_item())  # Смотрим результат

    # @pytest.mark.skip('[ISSUE-2341]')
    def test_json_validation(self, get_data_from_json):
        """Парсим и валидируем json."""
        get_data_from_json.validate(User)  # Валидируем объект
        print(get_data_from_json.get_parsed_item())  # Смотрим результат

    def test_user_count(self, get_data_from_response):
        """Проверяем длину словаря с данными."""
        assert len(get_data_from_response.data) == 10


class TestUsersMock:
    """Тесты с моками."""
    def test_status_code_positive(self, positive_response_mocker):
        """Проверяем статус-код."""
        assert positive_response_mocker.get().status_code == 200

    def test_status_code_negative(self, negative_response_mocker):
        """Проверяем статус-код."""
        with pytest.raises(AssertionError):
            assert negative_response_mocker.get().status_code == 200

    def test_response_validation_positive(self, positive_response_mocker):
        """Парсим и валидируем запрос."""
        for user in positive_response_mocker.get().json():
            User.parse_obj(user)

    def test_response_validation_negative(self, negative_response_mocker):
        """Парсим и валидируем запрос."""
        with pytest.raises(ValidationError):
            for user in negative_response_mocker.get().json():
                User.parse_obj(user)


if __name__ == '__main__':
    pytest.main()
