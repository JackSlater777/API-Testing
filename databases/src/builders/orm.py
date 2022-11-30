from databases.src.baseclasses.sessions import Model, engine_sqlite


def configure_orm():
    """Создание схемы."""
    Model.metadata.create_all(engine_sqlite)


def insert_orm(session, item):
    """Добавление записи."""
    session.add(item)
    session.commit()


def select_orm(session, table, filter_data):
    """Чтение всех записей."""
    items = session.query(table).filter(filter_data).order_by(table.item_id).all()
    return items


def update_orm(session, table, filter_data, updated_value):
    """Обновление записи."""
    session.query(table).filter(filter_data).update(updated_value)
    session.commit()


def delete_orm(session, table, filter_data):
    """Удаление записи."""
    session.query(table).filter(filter_data).delete()
    session.commit()
