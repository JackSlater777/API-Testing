# Тестируем: examples.py
# Схема: src/schemas/computer.py

# Запуск через терминал
# pytest -s -v tests/db/test_db.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v tests/db/test_db.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

# import pytest
# from src.baseclasses.response_2 import Response

import tables


# Делаем тестовый запрос к БД (если нет API)
# Получение сессии базы данных и использование её для того, чтобы достать
# нужную информацию.
# Getting database session. In the test, we get info from DB using the
# session.
def test_get_data_fields(get_db_session):
    data = get_db_session.querry(tables.Films).first()
    print(data.title)
    print(data.film_id)


# Удаляем данные из тестовой таблицы БД
#     Пример того, как использовать удаление в тесте, когда мы не знаем ID.
#     Просто получаем фикстуру которая умеет это делать и удаляем.
#     Если тест упадёт раньше, то до этой строки кода мы не дойдём, так как
#     удалять нечего, если же мы дошли, то удалять есть что :).
#     Example of case, when we know nothing about id that should be deleted from
#     DB after test execution. So in that case we just paste our method at the end
#     If our case fails we don't have to delete anything, if not
#     our code will do what it has to do :)
def test_try_to_delete_something(get_delete_method, get_db_session):
    # Метод 1 - создать сессию, выбрать нужные данные и удалить
    # Метод 2 - универсальный метод:
    # / по какой сессии, из какой таблицы дропнуть, по какому фильтру отфильтровать
    get_delete_method(get_db_session, tables.ItemType, (tables.ItemType.item_id == 3))


# Добавляем данные в тестовую таблицу БД
#     Добавление в базу тестовых данных в самом тесте, плохой пример, но может
#     пригодится. Лучше используйте фикстуры.
#     Adding test data into database in our test. It is a very bad example.
#     Please don't do like this.
def test_try_to_add_testdata(get_db_session, get_add_method, get_item_type_generator):
    # Приводим добавляемые данные к модели SQL-alchemy
    # new_item_type = {'item_type': 'MY_NEW_TYPE'}
    # item = tables.ItemType(**new_item_type)

    # Универсальный способ - создание случайных итемов
    item = tables.ItemType(**get_item_type_generator.build())
    # Добавляем
    get_add_method(get_db_session, item)
    print(item.item_id)


# Добавляем данные в тестовую таблицу БД, принтим, удаляем
#     Пример идеального флоу, когда мы создаём и удаляем после себя данные в базе
#     тем самым оставляя тест чистым.
#     PS: Смотрите фикстуру
#     Example of case, when we create and delete test data in our fixture.
#     PS: Check fixtures.
def test_try_to_add_testdata_and_delete_after_test(generate_item_type):
    print(generate_item_type.item_id)
