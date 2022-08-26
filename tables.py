# Здесь хранятся таблицы БД

from sqlalchemy import Boolean, Column, Integer, String
from db import Model


class Films(Model):
    # Описываем только те поля, которые нужны в работе
    # Имя таблицы
    __tablename__ = 'films'
    # Поля
    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)



