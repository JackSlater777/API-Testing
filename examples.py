from db import session
# from sqlalchemy.sql.expression import desc
import tables


# Делаем запросы к БД

# first - возвращает первый найденный результат
result = session.query(tables.Films.film_id, tables.Films.title).first()
# all - возвращает все результаты списком кортежей
result2 = session.query(tables.Films.film_id, tables.Films.title).all()
# one_or_none - возвращает конкретное условие кортежем
result3 = session.query(tables.Films.film_id, tables.Films.title).one_or_none()

# Запросы с фильтром
result4 = session.query(
    tables.Films.film_id, tables.Films.title
).filter(
    tables.Films.film_id == 180
).one_or_none()
if result:
    print("All is good")
else:
    print("Not good")

# Фильтр с несколькими условиями
result5 = session.query(
    tables.Films.film_id, tables.Films.title
).filter(
    tables.Films.film_id > 100,
    tables.Films.film_id < 150
).all()

# Вывод запроса на языке SQL с помощью subquery()
result6 = session.query(
    tables.Films.film_id
).filter(
    tables.Films.film_id > 180
).subquery()

# Фильтруем названия с помощью in_() - узнаем названия фильмов, которые есть в result6
result7 = session.query(
    tables.Films.title
).filter(
    tables.Films.film_id.in_(result6)
).all()

# Сортируем с помощью ordered_by()
result8 = session.query(
    tables.Films.film_id,
    tables.Films.title
).ordered_by(tables.Films.film_id).all()
# ).ordered_by(desc(tables.Films.film_id)).all()  # desc() - в обратном порядке

# Лимитируем количество результатов с помощью limit()
result9 = session.query(
    tables.Films.film_id,
    tables.Films.title
).ordered_by(tables.Films.film_id).limit(1).all()  # Вернет 1 ответ

# Пропускаем количество результатов с помощью offset()
result10 = session.query(
    tables.Films.film_id,
    tables.Films.title
).ordered_by(tables.Films.film_id).limit(1).offset(1).all()

print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)


# Пример объекта на котором вы можете потренироваться, используя pydantic схемы.
# Example of object for training with pydantic schemas.
computer = {
    "id": 21,
    "status": "ACTIVE",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": 'green',
            "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
        },
        "owners": [{
            "name": "Stephan Nollan",
            "card_number": "4000000000000002",
            "email": "shtephan.nollan@gmail.com",
        }]
    }
}
