from enum import Enum


class GlobalErrorMessages(Enum):

    # Обычный класс с ошибками которые стоит использовать в ваших Assert и в
    # Response класс. Нужно это для того, чтобы:
    # 1. Унифицировать всё это дело
    # 2. Облегчить использование и обновление ошибок

    # Default ENUM class with error that should be used in your asserts and in
    # Response class. It helps with:
    # 1. unification
    # 2. code support

    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected."
