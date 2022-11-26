import json
from pydantic.error_wrappers import ValidationError
from players.src.schemas.player import Player
from players.configuration import JSON_PATH


class ObjectValidator:
    """Главный класс валидации."""
    def __init__(self, data):
        self.data = data
        self.parsed_item = None

    def validate(self, schema):
        """Метод для разбирания объекта по pydantic-схеме."""
        try:
            # Если декодированный объект - список...
            if isinstance(self.data, list):
                # ...задаем контейнер для хранения...
                self.parsed_item = list()
                # ...каждый элемент в списке...
                for item in self.data:
                    # ...парсим по pydantic-схеме
                    parsed_item = schema.parse_obj(item)
                    self.parsed_item.append(parsed_item)

            # Если декодированный объект - словарь...
            else:
                # ...парсим по pydantic-схеме
                parsed_item = schema.parse_obj(self.data)
                self.parsed_item = parsed_item

        except ValidationError:
            # Allure помечает только те тесты failed, которые явно имеют какой-то AssertionError
            raise AssertionError("Could not map received object to pydantic schema!")

        return self

    def get_parsed_item(self):
        """Метод получения вывода спаршенного объекта."""
        return self.parsed_item


if __name__ == '__main__':
    # # Если используется mock-объект:
    # data = {
    #     "account_status": "ACTIVE",
    #     "balance": 10,
    #     "localize": {
    #             "en": {"nickname":  "SolveMe", "countries": {"UA": 3}},
    #             "ru": {"nickname":  "СолвМи"}
    #     },
    #     "avatar": "https://google.com"
    # }
    # obj = ObjectValidator(data)  # Скармливаем ответ в класс
    # obj.validate(Player)  # Валидируем ответ

    # Если используется json-файл:
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        data = json.load(read_file)
    obj = ObjectValidator(data)  # Скармливаем объект в класс
    obj.validate(Player)  # Валидируем объект
    print(obj.get_parsed_item())  # Смотрим результат
