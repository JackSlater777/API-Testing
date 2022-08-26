from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    # Если параметр необязательный: id: int = None
    name: str
    email: str
    # испортируем из enums возможные значения gender'a и status'a
    gender: Genders
    status: Statuses

    # Проверяем наличие знака @ в строке email'a
    @validator('email')
    def check_that_dog_presented_in_email_adress(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
