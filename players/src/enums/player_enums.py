from players.src.baseclasses.pyenum import PyEnum


class Statuses(PyEnum):
    """Перечисления для описания возможного статуса пользователя."""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"
    BANNED = "BANNED"


if __name__ == '__main__':
    print(Statuses.list())  # ['ACTIVE', 'INACTIVE', 'DELETED', 'BANNED']

    # # То же самое через list comprehension
    # status_list = [status.value for status in Statuses]
    # print(status_list)  # ['ACTIVE', 'INACTIVE', 'DELETED', 'BANNED']
