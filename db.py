# Файл базы данных

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from configuration import CONNECTION_ROW


# Создаем экземпляр для описания табличек
Model = declarative_base(name="Model")
# Создаем движок
engine = create_engine(
    CONNECTION_ROW
)
# Создаем сессию
Session = sessionmaker(
    engine,
    autoflush=False,  # Автообновление данных в БД
    autocommit=False  # Автокоммит
)
session = Session()
