from sqlalchemy import Column, Integer, String
from databases.src.baseclasses.sessions import Model


class ItemType(Model):
    """Описываем тестовую таблицу, в которую планируем вносить данные."""
    __tablename__ = 'ItemType'
    # Поля
    item_id = Column(Integer, primary_key=True)
    item_type = Column(String, nullable=False)
