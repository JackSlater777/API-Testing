import pytest
from databases.src.baseclasses import tables


class TestFilmsTable:
    """Тестируем таблицу фильмов в базе данных."""
    def test_films(self, get_db_session):
        """Получаем данные о фильмах."""
        data = get_db_session.query(tables.Films).first()  # Получаем первую match-запись из базы
        print(data.film_id)  # Смотрим id фильма
        print(data.title)  # Смотрим название фильма


class TestItemTypeTable:
    """Тестируем кастомную таблицу в базе данных."""
    def test_delete_data(self, get_db_session, delete_method):
        """Проверяем удаление данных с кастомным фильтром."""
        delete_method(  # Передаем...
            get_db_session,  # ...сессию,...
            tables.ItemType,  # ...таблицу, в которой нужно удалить данные...
            (tables.ItemType.item_id == 3)  # ...и то, что нужно удалить.
        )

    def test_add_data(self, build_and_add_item_type):
        """Проверяем добавление построенного объекта."""
        print(build_and_add_item_type)  # Смотрим сгенерированный id

    def test_add_and_delete_data(self, build_add_and_delete_item_type):
        """Пример идеального flow - создаём, добавляем и удаляем объект в базе,
        тем самым оставляя тест чистым."""
        print(build_add_and_delete_item_type)  # Смотрим сгенерированный id, но в базе его уже не будет


if __name__ == '__main__':
    pytest.main()
