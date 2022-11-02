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
from src.generators.player_localization import PlayerLocalization
from src.baseclasses.response import Response
from src.schemas.user import TestUser
from src.enums.user_enums import Statuses
from src.schemas.computer import Computer
from example_computers import computer


def test_getting_users(get_users, make_number, calculate):
    """
    Пример использования фикстуры которая отправляет запрос и возвращает
    респонс. Далее мы просто обрабатываем его с помощью нашего Response class
    применяя все доступные валидации.
    """
    # Запрос даты (убран в фикстуру)
    # response = requests.get(SERVICE_URL_2)
    # Прогоняем через класс (методы описаны в классе Response)
    # Response(get_users).assert_status_code(200).validate(TestUser)
    Response(get_users).assert_status_code(200)
    Response(get_users).validate(TestUser)
    # Выполняем глобальную фикстуру
    print(calculate(1, 1))
    # Выводим yield глобальной фикстуры
    print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_decorators():
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
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result',
                         [
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
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.parametrize('balance_value',
                         [
                             "100",
                             "0",
                             "-10",
                             "asd"
                         ])
def test_user_balance(balance_value, get_player_generator):
    """
    Тестируем баланс сгенерированных пользователей
    """
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize('status',
                         [
                             *Statuses.list()
                         ])
# или @pytest.mark.parametrize('status', Statuses.list())
def test_user_status(status, get_player_generator):
    """
    Тестируем статус сгенерированных пользователей (см. Enums).
    Играемся с генератором, который был получен с помощью фикстуры.
    Вы можете попробовать изменить значение, написать новые методы и посмотреть
    как он будет реагировать.
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('delete_key',
                         [
                             "account_status",
                             "balance",
                             "localize",
                             "avatar"
                         ])
def test_delete_user_attr(delete_key, get_player_generator):
    """
    Удаляем по одному свойству у пользователя и смотрим реакцию backend'a.
    Пример того, как мы в определённом порядке удаляем каждое поле в объекте,
    который нам вернул генератор.
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localisations, loc",
                         [
                             ("fr", "fr_FR")
                         ])
def test_update_user_localisation(get_player_generator, localisations, loc):
    """
    Тестируем обновление одного поля - локализации (с вложенностями).
    В этом примере мы получаем 2 генератора, один базовый и один - ниже
    уровнем. Когда мы получили их, изменяем в генераторе локализацию, создаём
    экземпляр и обновляем им наш главный объект.
    """
    object_to_send = get_player_generator.update_inner_value(
        ["localize", localisations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_pydantic_computer_object():
    """
    Пример того, как после инициализации pydantic объекта, можно получить
    доступ к любому из его параметров.
    """
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)
