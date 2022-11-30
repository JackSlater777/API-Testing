from sqlalchemy.orm import sessionmaker  # Для создания сессии
from sqlalchemy import create_engine  # Для создания движка
from sqlalchemy.ext.declarative import declarative_base  # Для моделей
from databases.configuration import DB_TYPE, DB_PATH


# Создаем класс Model, наследуясь от которого мы говорим engine, что это не
# просто python-object, а описанная таблица (в базе данных) на языке python.
Model = declarative_base(name="Model")

# Создаём соединение к базе данных, передавая креденшиалы и ссылку на БД.
# Для соединения по URL указываем этот URL вместо всего аргумента.
engine_sqlite = create_engine(f'{DB_TYPE}:///{DB_PATH}')

# Отправляем engine в sessionmaker, который, используя engine, знает к
# какой базе данных устанавливать соединение, а также кто и как будет туда
# отправлять данные.
Session_sqlite = sessionmaker(
    engine_sqlite,
    autoflush=False,
    autocommit=False
)
