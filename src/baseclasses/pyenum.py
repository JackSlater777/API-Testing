from enum import Enum


class PyEnum(Enum):

    # Возвращает список параметров, которые есть в enum
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
