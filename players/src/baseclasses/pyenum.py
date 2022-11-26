from enum import Enum


class PyEnum(Enum):
    """ENUM класс с методом представления перечислений в виде списка."""
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
