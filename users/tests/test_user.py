import pytest
from users.src.schemas.user import User
from pydantic import ValidationError
from users.src.baseclasses.response_validator import ResponseValidator
from users.src.baseclasses.object_validator import ObjectValidator


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
    def test_status_code(self, response):
        """Проверяем статус-код."""
        data = response.json().get("data")  # Конкретизируем данные под валидацию если необходимо - только data
        obj = ResponseValidator(response, data)  # Скармливаем объект в класс
        obj.assert_status_code(200)

    @pytest.mark.production
    def test_response_validation(self, response):
        """Парсим и валидируем запрос."""
        data = response.json().get("data")  # Конкретизируем данные под валидацию если необходимо - только data
        obj = ResponseValidator(response, data)  # Скармливаем объект в класс
        obj.validate(User)  # Валидируем объект
        print(obj.get_parsed_item())  # Смотрим результат

    # @pytest.mark.skip('[ISSUE-2341]')
    def test_json_validation(self, decode_json):
        """Парсим и валидируем json."""
        obj = ObjectValidator(decode_json)  # Скармливаем объект в класс
        obj.validate(User)  # Валидируем объект
        print(obj.get_parsed_item())  # Смотрим результат

    def test_user_count(self, response):
        """Проверяем длину словаря с данными."""
        data = response.json().get("data")  # Конкретизируем данные под валидацию если необходимо - только data
        obj = ResponseValidator(response, data)  # Скармливаем объект в класс
        assert len(obj.data) == 10


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
