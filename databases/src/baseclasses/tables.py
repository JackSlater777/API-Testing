from sqlalchemy import Boolean, Column, Integer, String
from databases.src.baseclasses.db import Model


class Films(Model):
    """Описываем таблицу с фильмами."""
    __tablename__ = 'films'
    # primary_key -> Хотя бы одно поле в табличке обязательно должно иметь такой параметр.
    # index -> Не обязательное к заполнению значение, но ускоряет построение запроса (см.индексирование);
    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)


class ItemType(Model):
    """Описываем тестовую таблицу, в которую планируем вносить данные."""
    __tablename__ = 'item_type'
    # Поля
    item_id = Column(Integer, primary_key=True)
    item_type = Column(String)
