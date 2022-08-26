from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    # Перечисляем разрешенные значения для параметра gender в схеме user'a
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    # Перечисляем разрешенные значения для параметра status в схеме user'a
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"
    BANNED = "BANNED"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"


print(Statuses.list())
