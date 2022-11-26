import json
from pydantic.error_wrappers import ValidationError
from computers.src.schemas.computer import Computer
from computers.configuration import JSON_PATH


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
    #     "id": 21,
    #     "status": "ACTIVE",
    #     "activated_at": "2013-06-01",
    #     "expiration_at": "2040-06-01",
    #     "host_v4": "91.192.222.17",
    #     "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    #     "detailed_info": {
    #         "physical": {
    #             "color": "green",
    #             "photo": "https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
    #             "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
    #         },
    #         "owners": [
    #             {
    #                 "name": "Stephan Nollan",
    #                 "card_number": "4000000000000002",
    #                 "email": "shtephan.nollan@gmail.com"
    #             }
    #         ]
    #     }
    # }
    # obj = ObjectValidator(data)  # Скармливаем ответ в класс
    # obj.validate(Player)  # Валидируем ответ

    # Если используется json-файл:
    with open(JSON_PATH, "r") as read_file:  # Декодируем json-файл в объект и помещаем в переменную
        data = json.load(read_file)
    obj = ObjectValidator(data)  # Скармливаем объект в класс
    obj.validate(Computer)  # Валидируем объект
    print(obj.get_parsed_item())  # Смотрим результат
