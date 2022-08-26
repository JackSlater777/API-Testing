# from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        # json-файл с данными
        self.response_json = response.json()
        # статус ответа
        self.response_status = response.status_code

    # Проверка json-файла на соответствие схеме
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)  # для pydantic
                # validate(item, schema)  # для jsonschema
        else:
            schema.parse_obj(self.response_json)  # для pydantic
            # validate(self.response_json, schema)  # для jsonschema
        return self

    # Проверка статуса кода
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
