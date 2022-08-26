# Описываем фикстуры для тестирования
import pytest
from random import randrange
from src.generators.player import Player


# scope='function' - по умолчанию - фикстура выполняется каждый тест кейс
# scope='session' - фикстура выполняется только 1 раз (удобно, когда надо логиться админом, коннектиться к БД)
# Если autouse=True, фикстуру аргументом передавать не нужно, она выполнится и без этого для каждого теста
# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


# Функция - как объект, передается в фикстуру (полезно при необходимости удалять\чистить какие-то данные)
def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate


# Нужна для чистки тестового пространства после теста (удалить тестовую БД и т.д.)
@pytest.fixture
def make_number():
    print("I'm getting a number")
    number = randrange(1, 1000, 5)
    # yield - переключение от фикстуры к тесту, после выполнения теста продолжится выполнение фикстуры
    yield number
    print(f"A number is {number}")


# Генерируем фикстурой рандомного пользователя
@pytest.fixture
def get_player_generator():
    return Player()
