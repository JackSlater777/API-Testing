# Тестируем:
# https://gorest.co.in/public/v1/users

# Запуск через терминал
# pytest -s -v tests/users/test_users.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v tests/users/test_users.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

import pytest
from src.generators.player_localisation import PlayerLocalisation
from src.baseclasses.response_2 import Response
from src.schemas.user import User
from src.enums.user_enums import Statuses


def test_getting_users_list(get_users, make_number, calculate):
    """
    Пример использования фикстуры которая отправляет запрос и возвращает
    респонс. Далее мы просто обрабатываем его с помощью нашего Response class
    применяя все доступные валидации.
    Example of using fixture that requesting server and returns raw response
    object. After it we put that data into our response class and accept all
    possible validation methods.
    """
    # Запрос даты (убран в фикстуру)
    # response = requests.get(SERVICE_URL_2)

    # Прогоняем через класс
    # Ассертим статус кода и валидэйтим юзера
    Response(get_users).assert_status_code(200).validate(User)
    # Выполняем глобальную фикстуру
    print(calculate(1, 1))
    # Выводим yield глобальной фикстуры
    print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_another():
    """
    Запуск через терминал тестов, замаркированных только маркером 'development':
    pytest -s -v -k development tests/users/test_users.py
    Запуск через терминал всех тестов, незамаркированных маркером 'development':
    pytest -s -v -k "not development" tests/users/test_users.py
    Маркировка теста - указываем, в какой категории деятельности используется данный тест
    Все маркеры указываются в ini-файле
    Можно указывать несколько маркеров столбиком
    Обычный тест, но не совсем. Обратите внимание на декораторы к нему.
    Мы скипаем его с определённым сообщением, а так же помечаем с каким скоупом
    его выполнять.
    It is just common test. Please check decorators of the test. Here is you
    can find decorator for skip test with some message and useful tags for
    case when you need to run some scope of tests.
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Вариант параметризации нашего теста, с несколькими параметрами за один
    раз.
    Example of parametrization, when during one iteration should be passed
    more than one value.
    """
    assert calculate(first_value, second_value) == result


# Тестируем баланс сгенерированных пользователей
@pytest.mark.parametrize('balance_value', [
    "100",
    "0",
    "-10",
    "asd"
])
def test_something1(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


# Тестируем статус сгенерированных пользователей (см. Enums)
#     Играемся с генератором, который был получен с помощью фикстуры.
#     Вы можете попробовать изменить значение, написать новые методы и посмотреть
#     как он будет реагировать.

#     Playing with generator, that we received from fixture.
#     Here you can change values, write some new useful methods and check how
#     will it work.
@pytest.mark.parametrize('status', [
    *Statuses.list()
])
# или @pytest.mark.parametrize('status', Statuses.list())
def test_something2(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# Удаляем по одному свойству у пользователя и смотрим реакцию backend'a
#     Пример того, как мы в определённом порядке удаляем каждое поле в объекте,
#     который нам вернул генератор.
#     Example of case when we delete one by one keys in received object.
@pytest.mark.parametrize('delete_key', [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_something3(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


# Тестируем обновление одного поля - локализации (с вложенностями)
#     В этом примере мы получаем 2 генератора, один базовый и один - ниже
#     уровнем. Когда мы получили их, изменяем в генераторе локализацию, создаём
#     экземпляр и обновляем им наш главный объект.
#     In the test we receive two generators, first is main and second is included
#     into first. We change localization in generator and update main using
#     instance of second.
@pytest.mark.parametrize("localisations, loc", [
    ("fr", "fr_FR")
])
def test_something4(get_player_generator, localisations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ["localize", localisations],
        PlayerLocalisation(loc).set_number(15).build()
    ).build()
    print(object_to_send)
