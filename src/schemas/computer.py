from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import validator
from pydantic import EmailStr  # Проверяет email
from pydantic.types import PastDate, FutureDate  # Проверяют дату (больше или меньше текущей)
from pydantic.types import PaymentCardNumber  # Проверяет номер карточки алгоритмом Luna
from pydantic.networks import IPv4Address, IPv6Address  # Проверяют IP

from src.enums.user_enums import Statuses
from src.schemas.physical import Physical

# Именно в этом файле можно поиграться с уже готовой моделью и примером
# тестового объекта для неё

from example_computer import computer  # То, что тестируем


# Создаем классы для каждой вложенности (матрёшку)
# В каждом классе можно дополнительно прописывать валидацию с помощью @validator

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr

    @validator('email')
    # Проверяем наше поле email, что в нём присутствует @ и в случае
    # если она отсутствует, возвращаем ошибку.
    # Checking fild email that in the filed contain @ and if it absent returns
    # error, if not pass.
    def check_that_dog_presented_in_email_adress(cls, email: str):
        if '@' not in email:
            raise ValueError("Email doesn't contain @")


class DetailedInfo(BaseModel):
    physical: Physical
    owners: list[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses  # импорт из Enums
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


try:
    comp = Computer.parse_obj(computer)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(comp)
    print(comp.schema_json())  # Генерируем json-схему
    print(comp.json())  # Генерируем json-файл

    print(comp.json(
        exclude={"status"}  # Синтаксис для вывода json без определенных атрибутов
    ))
