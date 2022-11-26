import pytest
from databases.src.baseclasses import tables
from databases.src.baseclasses.db import Session
from databases.src.builders.item_type import ItemTypeBuilder


@pytest.fixture
def get_db_session():
    """Фикстура для создания сессии с базой данных."""
    session = Session()  # Создаем сессию ...
    try:
        yield session  # ... и отдаем её в тест
    finally:
        session.close()  # Чтобы сессия не зависала в воздухе в случае разрыва соединения во время теста


def delete_data(session, table, filter_data):
    """Функция для удаления данных из таблицы."""
    session.query(table).filter(filter_data).delete()
    session.commit()


@pytest.fixture
def delete_method():
    """Фикстура для удаления данных из таблицы."""
    return delete_data


def add_data(session, item):
    """Функция для добавления данных в таблицу."""
    session.add(item)
    session.commit()


@pytest.fixture
def add_method():
    """Фикстура для удаления данных из таблицы."""
    return add_data


@pytest.fixture
def build_item_type():
    """Фикстура для строительства объекта в билдере."""
    return ItemTypeBuilder()  # Возвращаем построенный объект


@pytest.fixture
def build_and_add_item_type(get_db_session, build_item_type, add_method):
    """Фикстура, которая билдит и добавляет объект в таблицу."""
    item = tables.ItemType(**build_item_type.build())  # Декодим построенный объект под SQL-alchemy
    add_method(get_db_session, item)  # Добавляем объект в таблицу
    return item  # Возвращаем добавленный объект в тест, чтобы узнать о нем информацию


@pytest.fixture
def build_add_and_delete_item_type(get_db_session, build_and_add_item_type, delete_method):
    """Идеальный flow - фикстура, которая билдит, добавляет объект в таблицу и удаляет его после теста."""
    yield build_and_add_item_type  # См. фикстуру выше - билдим и добавляем
    delete_method(  # Удаляем объект из таблицы
        get_db_session,  # Передаем сессию...
        tables.ItemType,  # ...таблицу, в которой нужно удалить данные...
        (tables.ItemType.item_id == build_and_add_item_type.item_id)  # ...и то, что нужно удалить.
    )
