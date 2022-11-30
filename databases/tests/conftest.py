import pytest
import sqlite3
from databases.src.baseclasses.sessions import Session_sqlite
from databases.configuration import DB_PATH
from databases.src.builders.item_type import ItemTypeBuilder


@pytest.fixture
def build_item_type():
    """Фикстура для строительства объекта в билдере."""
    return ItemTypeBuilder()  # Возвращаем объект


# # # # # # # # # # # # # # # Для ORM SQLAlchemy
@pytest.fixture
def get_sqlite_session():
    """Фикстура для создания сессии с файлом SQLite."""
    session = Session_sqlite()  # Создаем сессию ...
    try:
        yield session  # ... и отдаем её в тест
    finally:
        session.close()  # Чтобы сессия не зависала в воздухе в случае разрыва соединения во время теста


# # # # # # # # # # # # # # # Для DB-API SQLite
@pytest.fixture
def get_sqlite_connect():
    """Фикстура для создания коннекта с файлом SQLite."""
    connection = sqlite3.connect(DB_PATH)
    try:
        yield connection  # Отдаем коннект в тест
    finally:
        connection.close()  # Чтобы сессия не зависала в воздухе в случае разрыва соединения во время теста
