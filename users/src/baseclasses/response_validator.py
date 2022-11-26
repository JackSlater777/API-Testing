import requests
import os
import json
from users.src.enums.error_enums import GlobalErrorMessages
from users.src.schemas.user import User
from users.src.baseclasses.object_validator import ObjectValidator
from users.configuration import SERVICE_URL, JSON_PATH, FOLDER_PATH


class ResponseValidator(ObjectValidator):
    """Класс принимает ответ, выводит по нему информацию и подготавливает объект к валидации."""
    def __init__(self, response, data):
        super().__init__(data)
        self.response = response
        self.data = data  # Вытаскиваем из декодированного объекта нужные данные
        self.response_status_code = response.status_code

    def get_full_info(self):
        """Вывод подробной информации об ответе."""
        print(self.response.__getstate__())

    def __str__(self):
        """Строковый вывод ответа."""
        return \
            f"\nStatus code: {self.response_status_code} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.data}"

    def assert_status_code(self, status_code):
        """Метод проверки статус кода."""
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, f"\n{GlobalErrorMessages.WRONG_STATUS_CODE.value} {self}"
        else:
            assert self.response_status_code == status_code, f"\n{GlobalErrorMessages.WRONG_STATUS_CODE.value} {self}"
        return self

    def save_response_json(self, folder_path=FOLDER_PATH, file_path=JSON_PATH):
        """Метод для сохранения ответа в json-файл."""
        create_folder(folder_path)  # Создаем папку
        # Выгружаем ответ в json-файл
        with open(file_path, "w") as write_file:
            json.dump(self.response.json(), write_file, sort_keys=True, indent=4)


def create_folder(folder_path) -> None:
    """Функция создания папки - для json-файлов."""
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


if __name__ == '__main__':
    # Если валидируем ответ от сервера:
    r = requests.get(SERVICE_URL)  # Делаем запрос
    data = r.json().get("data")  # Конкретизируем данные под валидацию если необходимо (только data, без meta)
    response = ResponseValidator(r, data)  # Скармливаем ответ в класс
    response.validate(User)  # Валидируем ответ
    print(response)  # Смотрим результат
    response.save_response_json()  # Сохраняем ответ в json-файл
