def configure_db(connect):
    """Создание базы данных."""
    cur = connect.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ItemType
                (item_id     INTEGER   PRIMARY KEY   AUTOINCREMENT,
                 item_type   TEXT      NOT NULL)''')


def insert_dbapi(connect, item: dict):
    """Добавление записи."""
    cur = connect.cursor()
    # cur.execute(
    #     '''INSERT INTO ItemType (item_id, item_type)
    #     VALUES (:id, :type)''',
    #     {'id': item['item_id'], 'type': item['item_type']}
    # )
    # Более изящный способ
    cur.execute(
        '''INSERT INTO ItemType
        VALUES (?, ?)''',
        list(item.values())
    )
    connect.commit()


def find_the_highest_id(connect):
    """Установление самого большого id."""
    cur = connect.cursor()
    cur.execute(
        '''SELECT item_id FROM ItemType
        ORDER BY item_id DESC'''
    )
    return cur.fetchone()


def select_dbapi(connect):
    """Чтение всех записей."""
    cur = connect.cursor()
    cur.execute(
        '''SELECT * FROM ItemType'''
    )
    return cur.fetchall()


def update_dbapi(connect, item: dict):
    """Обновление записи."""
    cur = connect.cursor()
    cur.execute(
        '''UPDATE ItemType
        SET item_type = :new_item_type
        WHERE item_id = :id''',
        {'id': item['item_id'], 'new_item_type': item['item_type']}
    )
    connect.commit()


def delete_dbapi(connect, item: dict):
    """Удаление записи."""
    cur = connect.cursor()
    cur.execute(
        '''DELETE FROM ItemType
        WHERE item_id = :id''',
        {'id': item['item_id']}
    )
    connect.commit()
