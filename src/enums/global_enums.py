from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected."


def test_something(status, get_player_generator):
    print(get_player_generator.build())
