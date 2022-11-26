from enum import Enum


# !!! ВНИМАНИЕ !!! Без указания в аргументах str при тесте валидации:
# Class.enum_name.value = <Class.enum_name: 'value'>
# При assert сравнении со строкой тест будет ПАДАТЬ!!!, т.к.
# <Class.enum_name: 'value'> != 'value'

# С указанием в аргументах str:
# Genders.female.value = 'female'


class Genders(str, Enum):
    """Перечисления для описания возможного пола пользователя."""
    female = "female"
    male = "male"


class Statuses(str, Enum):
    """Перечисления для описания возможного статуса пользователя."""
    inactive = "inactive"
    active = "active"
