# Файл базы данных
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from configuration import CONNECTION_ROW


# Создаём модель для того, чтобы потом использовать её для описания наших таблиц.
Model = declarative_base(name="Model")

# Создаём коннекшен к нашей базе данных, передавая ему креденшеналы и другую
# информацию для этого. Пример коннекшен строки вы можете найти в файле configuration.py.
engine = create_engine(CONNECTION_ROW)

# Создаём экземпляр сессии, которая даст нам возможность каждый раз генерировать
# новую сессию.
Session = sessionmaker(
    engine,
    autoflush=False,  # Автообновление данных в БД
    autocommit=False  # Автокоммит
)
session = Session()
