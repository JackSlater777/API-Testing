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


if __name__ == '__main__':
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
