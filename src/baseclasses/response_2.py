# from jsonschema import validate
# from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        # json-файл с данными
        self.response_json = response.json().get('data')
        # статус ответа
        self.response_status = response.status_code
        # По умолчанию объект необработан
        self.parsed_object = None

    # Проверка json-файла на соответствие схеме
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # для pydantic
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
                # для jsonschema
                # validate(item, schema)
        else:
            schema.parse_obj(self.response_json)  # для pydantic
            # validate(self.response_json, schema)  # для jsonschema
        return self

    # Возвращает обработанный pydantic'ом объект
    def get_parsed_object(self):
        return self.parsed_object

    # Проверка статуса кода
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    # Строковое представление класса
    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
