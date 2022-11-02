import requests
from pydantic.error_wrappers import ValidationError
from configuration import SERVICE_URL
from src.schemas.user import TestUser


class Response:
    """
    Полезный класс, который помогает нам экономить тонны кода в процессе
    валидации данных. На вход он принимает объект респонса и разбирает его.
    Вы можете добавить кучу различных методов в этом классе, которые нужны
    вам в работе с данными после их получения.
    """
    def __init__(self, response):
        self.response = response
        # json-файл с данными
        self.response_json = response.json()
        # статус ответа
        self.response_status = response.status_code
        # По умолчанию объект необработан
        self.parsed_object = None

    def validate(self, schema):
        """Проверка json-файла на соответствие схеме"""
        try:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object
                    print(f'{self.parsed_object=}')
            elif isinstance(self.response_json, dict):
                if 'data' in self.response_json:
                    for item in self.response_json['data']:
                        parsed_object = schema.parse_obj(item)
                        self.parsed_object = parsed_object
                        print(f'{self.parsed_object=}')
            else:
                schema.parse_obj(self.response_json)

        except ValidationError:
            raise AssertionError(
                "Could not map received object to pydantic schema"
            )

    def assert_status_code(self, status_code):
        """
        Метод для валидации статус кода. Из полученного объекта респонса
        мы берём статус и сравнимаем с тем, который нам был передан как параметр.
        """
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        """
        Возвращает обработанный pydantic'ом объект
        """
        return self.parsed_object

    def __str__(self):
        """
        Метод отвечает за строковое представление нашего объекта. Что весьма
        удобно, ведь в случае срабатывания валидации, мы получаем полную картину
        всего происходящего и все параметры, которые нам нужны для определения
        ошибки.
        """
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"


if __name__ == '__main__':
    response = Response(requests.get(SERVICE_URL))
    # print(response)  # Выводится инфа методом __str__
    print(type(response))  # <class '__main__.Response'>
    print(type(response.response_json))  # <class 'dict'>
    print("\n")
    # Выводим словари с информацией о каждом пользователе
    for user in response.response_json['data']:
        print(f'{user=}')
        try:
            # Парсим по соответствующей pydantic-схеме простенький json пользователя
            parsed_user = TestUser.parse_obj(user)
        except ValidationError as e:
            print("Exception", e.json())
        else:
            print(f'{parsed_user=}')
            print(f'{parsed_user.schema_json()=}')  # Генерируем json-схему
            print(f'{parsed_user.json()=}')  # Генерируем json-файл
            print("\n")
