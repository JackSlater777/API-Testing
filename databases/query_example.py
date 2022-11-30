from databases.src.baseclasses import tables
from databases.src.baseclasses.sessions import Session_postgres
from sqlalchemy.sql.expression import desc  # Обратная сортировка


if __name__ == '__main__':
    # Получаем соединение через session-экземпляр.
    session = Session_postgres()

    # first() - возвращает только первый найденный результат
    result1 = session.query(tables.Films.film_id, tables.Films.title).first()
    print(result1)  # (183, 'Дорога пробуждения')

    # all() - возвращает все результаты списком
    result2 = session.query(tables.Films.film_id, tables.Films.title).all()
    print(result2)  # [(183, 'Дорога пробуждения'), (107, 'Девчата'), (108, 'Хоббит: Неожиданное путешествие')

    # one_or_none() - возвращает только один результат с конкретным условием
    result3 = session.query(tables.Films.film_id, tables.Films.title).one_or_none()
    print(result3)  # raise exc.MultipleResultsFound()

    # filter() - отфильтровывает результат по заданным критериям
    result4 = session.query(
        tables.Films.film_id, tables.Films.title
    ).filter(
        tables.Films.film_id == 180
    ).one_or_none()
    print(result4)  # (180, 'Окно во двор')

    result5 = session.query(
        tables.Films.film_id, tables.Films.title
    ).filter(
        tables.Films.film_id > 100,
        tables.Films.film_id < 150
    ).all()
    print(result5)  # [(107, 'Девчата'), (108, 'Хоббит: Неожиданное путешествие'), (112, 'Мальчик в полосатой пижаме'...

    # subquery() - вывод запроса на языке SQL
    result6 = session.query(
        tables.Films.film_id
    ).filter(
        tables.Films.film_id > 180
    ).subquery()
    print(result6)
    # SELECT films.film_id
    # FROM films
    # WHERE films.film_id > :film_id_1

    # in_() - доп. конструкция к filter(), возвращает все результаты, которые есть в result6
    result7 = session.query(
        tables.Films.title
    ).filter(
        tables.Films.film_id.in_(result6)
    ).all()
    print(result7)  # [('Тхэджон Ли Банвон',), ('Развод по-английски',), ('Дорога пробуждения',), ... ]

    # order_by() - сортирует по параметру вывод результата от меньшего к большему
    result8 = session.query(
        tables.Films.film_id
    ).order_by(
        tables.Films.film_id
    ).all()
    print(result8)  # [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), ...]

    # ordered_by(desc()) - сортирует по параметру вывод результата от большего к меньшему
    result9 = session.query(
        tables.Films.film_id,
        tables.Films.title
    ).order_by(
        desc(tables.Films.film_id)
    ).all()
    print(result9)  # [(193,), (192,), (191,), (190,), (189,), (188,), (187,), (186,), ...]

    # limit() - лимитирует количество возвращаемых результатов
    result10 = session.query(
        tables.Films.film_id,
        tables.Films.title
    ).order_by(tables.Films.film_id).limit(1).all()  # Вернет 1 ответ
    print(result10)  # [(193, 'Глубокое синее море')]

    # offset() - пропускает (skip) количество результатов
    result11 = session.query(
        tables.Films.film_id,
        tables.Films.title
    ).order_by(tables.Films.film_id).limit(1).offset(1).all()
    print(result11)  # [(192, 'Начальник разведки')]
