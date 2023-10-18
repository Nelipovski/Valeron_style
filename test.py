import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()


cursor.execute(
    '''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

conn.close()


def create_query(template: str, data: tuple):
    """
    Accepts query type and user data as input.
    No fetch.
    """
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        log.info("Connection to SQLite DB successful")
        cursor = connection.cursor()
        cursor.execute(template, data)
        connection.commit()
        cursor.close()
        log.info("Query executed successfully")

    except Error as e:
        log.error(f"The error '{e}' occurred")
        return e
    finally:
        if connection:
            connection.close()
            log.info("Connection to SQLite DB closed")
