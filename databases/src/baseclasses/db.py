from sqlalchemy.orm import sessionmaker  # Для создания сессии
from sqlalchemy import create_engine  # Для создания движка
from sqlalchemy.ext.declarative import declarative_base  # Для моделей
from databases.configuration import CONNECTION_ROW

# Создаем класс Model, наследуясь от которого мы говорим engine, что это не
# просто python-object, а описанная таблица (в базе данных) на языке python.
Model = declarative_base(name="Model")

# Создаём соединение к базе данных, передавая креденшиалы и ссылку на БД.
engine = create_engine(CONNECTION_ROW)

# Отправляем engine в sessionmaker, который, используя engine, знает к
# какой базе данных устанавливать соединение, а также кто и как будет туда
# отправлять данные.
Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)
