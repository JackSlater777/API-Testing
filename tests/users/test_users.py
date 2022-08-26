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


# response = requests.get(SERVICE_URL_2)
# print(response.json)
# print(response.__getstate__())
# print(response.url)

# z = {
#     "meta": {
#         "pagination": {
#             "total": 1725,
#             "pages": 87,
#             "page": 1,
#             "limit": 20,
#             "links": {
#             }
#         }
#     },
#     "data": {
#         {
#             "id": 1753,
#             "name": "API Monitoring:5y3",
#             "email": "apimonitoring5y3at@synthetic.com",
#             "gender": "femail",
#             "status": "inactive"
#         }
#     }
# }


# В аргументе фикстуры, запускаются до теста: одна - локальная, другие - глобальные
def test_getting_users_list(get_users, make_number, calculate):
    """
    Здесь указываем описание теста (появится в allure-description)
    """
    # Запрос даты (убран в фикстуру)
    # response = requests.get(SERVICE_URL_2)
    # Прогоняем через класс
    test_object = Response(get_users)
    # Ассертим статус кода и валидэйтим юзера
    test_object.assert_status_code(200).validate(User)
    # Выполняем глобальную фикстуру
    print(calculate(1, 1))
    # Выводим yield глобальной фикстуры
    print(make_number)


# Декоратор для пропуска теста
# В качестве параметра указывается reason - причина пропуска (для удобства)
@pytest.mark.skip('Issue with network connection - not critical')
def test_another():
    """
    Здесь указываем описание теста (появится в allure-description)
    """
    assert 1 == 1


# Запуск через терминал тестов, замаркированных только маркером 'development':
# pytest -s -v -k development tests/users/test_users.py
# Запуск через терминал всех тестов, незамаркированных маркером 'development':
# pytest -s -v -k "not development" tests/users/test_users.py
# Маркировка теста - указываем, в какой категории деятельности используется данный тест
# Все маркеры указываются в ini-файле
# Можно указывать несколько маркеров столбиком
@pytest.mark.development
# Декоратор для параметризации теста
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Здесь указываем описание теста (появится в allure-description)
    """
    assert calculate(first_value, second_value) == result


# Структура текущего пользователя (json) - для тестов ниже:
# player = {
#     "account_status": "active",
#     "balance": 10,
#     "localize": {
#         "en": {"nickname": "SolveMe", "countries":{"UA": 3}},
#         "ru": {"nickname": "СолвМи"}
#     },
#     "avatar": "https://google.com"
# }

# Тестируем баланс сгенерированных пользователей
@pytest.mark.parametrize('balance_value', [
    "100",
    "0",
    "-10",
    "asd"
])
def test_something1(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


# Тестируем статус сгенерированных пользователей (см. Enums
@pytest.mark.parametrize('status', [
    *Statuses.list()
])
# или @pytest.mark.parametrize('status', Statuses.list())
def test_something2(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# Удаляем по одному свойству у пользователя и смотрим реакцию backend'a
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
@pytest.mark.parametrize("localisations, loc", [
    ("fr", "fr_FR")
])
def test_something4(get_player_generator, localisations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ["localize", localisations],
        PlayerLocalisation(loc).set_number(15).build()
    ).build()
    print(object_to_send)


# Тесты для компьютера
def test_pydantic_object():
    pass
