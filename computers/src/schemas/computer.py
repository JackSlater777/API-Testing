from pydantic import BaseModel, conint
from pydantic import EmailStr  # Проверяет email
from pydantic.types import PastDate, FutureDate  # Проверяет дату
from pydantic.types import PaymentCardNumber  # Проверяет номер карты алгоритмом Luna
from pydantic.networks import IPv4Address, IPv6Address  # Проверяет IP-адрес
from pydantic import HttpUrl  # Проверяет Url
from pydantic import UUID4  # Проверяет UUID
from pydantic.color import Color  # Проверяет цвет
from computers.src.enums.computer_enums import Statuses


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class DetailedInfo(BaseModel):
    physical: Physical
    owners: list[Owners]


class Computer(BaseModel):
    id: conint(strict=True)  # Чтобы избежать конвертации строки в число pydantic'oм
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo
