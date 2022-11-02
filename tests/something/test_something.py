# Тестируем:
# https//:my-json-server.typicode.com/typicode/demo/posts

# Запуск через терминал
# pytest -s -v tests/something/test_something.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v tests/something/test_something.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

import requests
import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses
from src.baseclasses.response import Response
from src.schemas.computer import Inventory

import tables


# В этом файле рассмотрим примеры работы:
#  1. С базой данных
#  2. Параметризация ключей и поочерёдное их удаление
#  3. Использование генератора в тестах
#  4. Кастомная генерацию локализаций


@pytest.mark.parametrize("status", Statuses.list())
def test_changing_status(status, get_player_generator):
    """
    Играемся с генератором, который был получен с помощью фикстуры.
    Вы можете попробовать изменить значение, написать новые методы и посмотреть
    как он будет реагировать.
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_deleting_players_attr(delete_key, get_player_generator):
    """
    Пример того, как мы в определённом порядке удаляем каждое поле в объекте,
    который нам вернул генератор.
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_updating_localization_in_generator(
        get_player_generator,
        localizations,
        loc
):
    """
    В этом примере мы получаем 2 генератора, один базовый и один, который ниже
    уровнем. Когда мы получили их, изменяем в генераторе локализацию, создаём
    экземпляр и обновляем им наш главный объект.
    """
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_human():
    """
    Пример отправки запроса, получения данных и использования Response class
    для работы с валидацией данных.
    """
    r = requests.get('https://petstore.swagger.io/v2/store/inventory')
    response = Response(r)
    response.validate(Inventory)


def test_get_data_films(get_db_session):
    """
    Получение сессии базы данных и использование её для того, чтобы достать
    нужную информацию.
    """
    data = get_db_session.query(tables.Films).first()
    print(data.film_id)


def test_try_to_delete_something(get_delete_method, get_db_session):
    """
    Пример того, как использовать удаление в тесте, когда мы не знаем ID.
    Просто получаем фикстуру которая умеет это делать и удаляем.
    Если тест упадёт раньше, то до этой строки кода мы не дойдём, так как
    удалять нечего. Если же мы дошли, то удалять есть что :).
    """
    get_delete_method(
        get_db_session,
        tables.ItemType,
        (tables.ItemType.item_id == 3)
    )


def test_try_to_add_testdata(
        get_db_session,
        get_add_method,
        get_item_type_generator
):
    """
    Добавление в базу тестовых данных в самом тесте, плохой пример но может
    пригодится. Лучше используйте фикстуры.
    """
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(item.item_id)


def test_try_to_add_testdata_and_delete_after_the_test(generate_item_type):
    """
    Пример идеального флоу, когда мы создаём и удаляем после себя данные в базе
    тем самым оставляя тест чистым.
    PS: Смотрите фикстуру.
    """
    print(generate_item_type.item_id)
