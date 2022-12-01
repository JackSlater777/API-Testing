import os
import pytest
from databases.configuration import DB_PATH
from databases.src.baseclasses import tables
from databases.src.builders.sqlite import configure_db, insert_dbapi, select_dbapi, update_dbapi, delete_dbapi, find_the_highest_id
from databases.src.builders.orm import configure_orm, insert_orm, select_orm, update_orm, delete_orm, clear_orm


class TestItemTypeTableSQLite:
    """Тестируем таблицу в базе данных SQLite через DB-API."""
    def test_create_itemtype_table(self, get_sqlite_connect):
        """Проверяем создание базы данных."""
        configure_db(get_sqlite_connect)  # Передаем коннект в метод создания таблицы
        assert os.path.exists(DB_PATH)

    def test_build_and_insert_item(self, get_sqlite_connect, build_item_type):
        """Проверяем добавление данных."""
        item = build_item_type.build()  # Строим объект
        insert_dbapi(get_sqlite_connect, item)  # Добавляем объект в базу
        print(item['item_id'], item['item_type'])  # id остался None - недостаток DB-API

    def test_select_all_items(self, get_sqlite_connect):
        """Проверяем чтение всех данных."""
        print(select_dbapi(get_sqlite_connect))

    def test_update_item(self, get_sqlite_connect):
        """Проверяем обновление данных."""
        item = {'item_id': 1, 'item_type': 'Robert'}  # Указываем обновленный объект, который должен быть
        update_dbapi(get_sqlite_connect, item)  # Заменяем значение по id

    def test_delete_item(self, get_sqlite_connect):
        """Проверяем удаление данных с кастомным фильтром."""
        item = {'item_id': 611}  # Указываем объект
        delete_dbapi(get_sqlite_connect, item)  # Удаляем объект из базы

    def test_find_max_id(self, get_sqlite_connect):
        """Проверяем максимальный id."""
        print(find_the_highest_id(get_sqlite_connect)[0])  # max id

    def test_build_insert_and_delete_item(self, get_sqlite_connect, build_item_type):
        """Пример идеального flow - создаём, добавляем и удаляем объект в базе,
        тем самым оставляя тест чистым."""
        item = build_item_type.build()  # Строим объект
        insert_dbapi(get_sqlite_connect, item)  # Добавляем объект в базу
        print(item)  # Смотрим id и имя, но в базе их уже не будет
        item_id = find_the_highest_id(get_sqlite_connect)[0]  # Находим id добавленного объекта
        item = {'item_id': item_id}  # Указываем объект
        delete_dbapi(get_sqlite_connect, item)  # Удаляем объект из базы


class TestItemTypeTableORM:
    """Тестируем таблицу в базе данных SQLite через ORM SQLAlchemy."""
    def test_create_itemtype_table(self):
        """Проверяем создание базы данных."""
        configure_orm()  # Передаем коннект в метод создания таблицы
        assert os.path.exists(DB_PATH)

    def test_build_and_insert_item(self, get_sqlite_session, build_item_type):
        """Проверяем добавление данных."""
        item = tables.ItemType(**build_item_type.build())  # Строим и декодим объект под модель ItemType
        insert_orm(get_sqlite_session, item)  # Добавляем объект в базу
        print(item.item_id, item.item_type)  # id изменился с None на max

    def test_select_all_items(self, get_sqlite_session):
        """Проверяем чтение всех данных c упорядочиванием по первичному ключу."""
        items = select_orm(
            get_sqlite_session,  # ...сессию,...
            tables.ItemType,  # ...таблицу,...
            (tables.ItemType.item_id > 0)  # ...и то, что нужно прочитать.
        )
        for item in items:
            print(item.item_id, item.item_type)

    def test_update_item(self, get_sqlite_session):
        """Проверяем обновление данных."""
        item = {'item_id': 1, 'item_type': 'Robert'}  # Указываем обновленный объект, который должен быть
        update_orm(  # Передаем...
            get_sqlite_session,  # ...сессию,...
            tables.ItemType,  # ...таблицу,...
            (tables.ItemType.item_id == item['item_id']),  # ...id объекта, который нужно изменить...
            {tables.ItemType.item_type: item['item_type']}  # ...и новое значение, которое ему нужно подставить
        )

    def test_delete_item(self, get_sqlite_session):
        """Проверяем удаление данных с кастомным фильтром."""
        item_id = 611    # Указываем фильтр объекта
        delete_orm(  # Передаем...
            get_sqlite_session,  # ...сессию,...
            tables.ItemType,  # ...таблицу,...
            (tables.ItemType.item_id == item_id)  # ...и то, что нужно удалить.
        )

    def test_build_insert_and_delete_item(self, get_sqlite_session, build_item_type):
        """Пример идеального flow - создаём, добавляем и удаляем объект в базе,
        тем самым оставляя тест чистым."""
        item = tables.ItemType(**build_item_type.build())  # Строим и декодим объект под модель ItemType
        insert_orm(get_sqlite_session, item)  # Добавляем объект в базу
        print(item.item_id, item.item_type)  # Смотрим id и имя, но в базе их уже не будет
        delete_orm(  # Передаем...
            get_sqlite_session,  # ...сессию,...
            tables.ItemType,  # ...таблицу,...
            (tables.ItemType.item_id == item.item_id)  # ...и то, что нужно удалить.
        )

    def test_delete_itemtype_table(self):
        """Удаление таблицы ItemType."""
        clear_orm()  # Передаем коннект в метод создания таблицы


if __name__ == '__main__':
    pytest.main()
