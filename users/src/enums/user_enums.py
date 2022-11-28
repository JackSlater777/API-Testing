from users.src.baseclasses.pyenum import PyEnum


# !!! ВНИМАНИЕ !!! Без наследования от str при тесте валидации:
# Class.enum_name.value = <Class.enum_name: 'value'>
# При assert сравнении со строкой тест будет ПАДАТЬ!!!, т.к.
# <Class.enum_name: 'value'> != 'value'

# С наследованием от str:
# Genders.female.value = 'female'


class Genders(str, PyEnum):
    """Перечисления для описания возможного пола пользователя."""
    female = "female"
    male = "male"


class Statuses(str, PyEnum):
    """Перечисления для описания возможного статуса пользователя."""
    inactive = "inactive"
    active = "active"


if __name__ == '__main__':
    print(Genders.list())  # ['female', 'male']
    print(Statuses.list())  # ['inactive', 'active']

    # # То же самое через list comprehension
    # gender_list = [gender.value for gender in Genders]
    # print(gender_list)  # ['inactive', 'active']
    # status_list = [status.value for status in Statuses]
    # print(status_list)  # ['inactive', 'active']
