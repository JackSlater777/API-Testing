from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, Status, UserErrors
from pydantic import EmailStr  # Проверяет email
from pydantic.error_wrappers import ValidationError

from example_users import response_body  # То, что тестируем.
# Это уже обработанный запрос, который можно получить так:
# response = requests.get("https://gorest.co.in/public/v1/users").json()
# print(response)


class User(BaseModel):
    """
    Пример описания pydantic model с использованием Enum и validator.
    """
    id: int  # Если параметр необязательный: id: int = None
    name: str
    email: str
    # испортируем из enums возможные значения gender'a и status'a
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_adress(cls, email):
        """
        Проверяем наше поле email, что в нём присутствует @ и в случае
        если она отсутствует, возвращаем ошибку.
        Checking fild email that in the filed contain @ and if it absent returns
        error, if not pass.
        """
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)


class TestUser(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: Genders
    status: Status


if __name__ == '__main__':
    # Выводим словари с информацией о каждом пользователе
    if 'data' in response_body:
        try:
            # Парсим по соответствующей pydantic-схеме каждого пользователя
            for item in response_body['data']:
                test_user = TestUser.parse_obj(item)
                print(f'{test_user=}')
                print(f'{test_user.schema_json()=}')  # Генерируем json-схему
                print(f'{test_user.json()=}')  # Генерируем json-файл
                print('\n')
        except ValidationError as e:
            print("Exception", e.json())
