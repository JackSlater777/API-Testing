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
    It's a useful class that helps to save a lot of code during validation
    process in our tests. It receives a response object and gets from it all
    values that should be validated. You can add additional methods into the
    Class if it needs for your project testing.
    """
    def __init__(self, response):
        self.response = response
        # json-файл с данными
        self.response_json = response.json()
        # статус ответа
        self.response_status = response.status_code
        # По умолчанию объект необработан
        self.parsed_object = None

    # Проверка json-файла на соответствие схеме
    def validate(self, schema):
        try:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object
            elif isinstance(self.response_json, dict):
                if 'data' in self.response_json:
                    for item in self.response_json['data']:
                        parsed_object = schema.parse_obj(item)
                        self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.response_json)
        except ValidationError:
            raise AssertionError(
                "Could not map received object to pydantic schema"
            )

    # Проверка статуса кода
    def assert_status_code(self, status_code):
        """
        Метод для валидации статус кода. Из объекта респонса,
        который мы получили, мы берём статус и сравнимаем с тем, который
        нам был передан как параметр.
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    # Возвращает обработанный pydantic'ом объект
    def get_parsed_object(self):
        return self.parsed_object

    # Строковое представление объекта
    def __str__(self):
        """
        Метод отвечает за строковое представление нашего объекта. Что весьма
        удобно, ведь в случае срабатывания валидации, мы получаем полную картину
        всего происходящего и все параметры которые нам нужны для определения
        ошибки.
         Method for string displaying of class instance. In case when our
         validation will be failed, we will get full information about our
         object and data, that will help us in fail investigation.
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
