import psycopg2
import time
time.sleep(1)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    return conn

def setup_database(cursor):
    # Создаем таблицу
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    );
    """)

def clear_table(cursor):
    # Очищаем таблицу перед каждым тестом
    cursor.execute("DELETE FROM users;")

def test_database_connection():
    conn = get_db_connection()
    assert conn is not None

def test_data_insertion():
    conn = get_db_connection()
    cursor = conn.cursor()
    setup_database(cursor)
    clear_table(cursor)
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")

def test_data_update():
    conn = get_db_connection()
    cursor = conn.cursor()
    setup_database(cursor)
    clear_table(cursor)

    # Вставляем данные
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()

    # Обновляем имя пользователя с id=1
    cursor.execute("UPDATE users SET name = 'Jane' WHERE id=1")
    conn.commit()

    # Проверяем, что имя обновилось
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'Jane'

def test_data_deletion():
    conn = get_db_connection()
    cursor = conn.cursor()
    setup_database(cursor)
    clear_table(cursor)

    # Вставляем данные для удаления
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()

    # Удаляем запись с id=1
    cursor.execute("DELETE FROM users WHERE id=1")
    conn.commit()

    # Проверяем, что запись удалена
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result is None

def test_data_selection():
    conn = get_db_connection()
    cursor = conn.cursor()
    setup_database(cursor)
    clear_table(cursor)

    # Вставляем несколько записей
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    cursor.execute("INSERT INTO users (id, name) VALUES (2, 'Alice')")
    conn.commit()

    # Выбираем все записи из таблицы users
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    # Проверяем, что выбрано 2 записи
    assert len(result) == 2
    assert result[0][1] == 'John'
    assert result[1][1] == 'Alice'