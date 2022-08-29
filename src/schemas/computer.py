from pydantic import BaseModel
from pydantic import EmailStr  # Проверяет email
from pydantic.types import PastDate, FutureDate  # Проверяют дату (больше или меньше текущей)
from pydantic.types import PaymentCardNumber  # Проверяет номер карточки алгоритмом Luna
from pydantic.types import List
from pydantic.networks import IPv4Address, IPv6Address  # Проверяют IP

from src.enums.user_enums import Statuses
from src.schemas.physical import Physical

from examples import computer  # То, что взято за пример


# Создаем классы для каждой вложенности (матрёшку)
# В каждом классе можно дополнительно прописывать валидацию с помощью @validator
# В идеале для каждого сервиса(класса) создаем отдельный файл !!!!!!!

# Именно в этом файле можно поиграться с уже готовой моделью и примером
# тестового объекта для неё (Human).

# That file gives to you possibility to play with ready to use model (Human).

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses  # импорт из Enums
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp)
print(comp.schema_json())  # Генерируем json-схему
