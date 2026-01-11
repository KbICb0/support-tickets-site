import sqlite3
# Устанавливаем соединение с базой данных

DB_NAME = "support_tickets_sqlite.db"

def get_connection():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    return connection, cursor


# Создаем таблицу Users
def create_table_users():
    conn, cursor = get_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    email TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

#Вставка данных
def create_user(id, username, password, role, email):
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (id, username, password, role, email))
    conn.commit()
    conn.close()

#Запрос данных
def get_users():
    conn, cursor = get_connection()
    cursor.execute("""
    SELECT * FROM Users
    """)
    result = cursor.fetchall()
    print(result)
    conn.commit()
    conn.close()
    


if __name__ == "__main__":
    create_user(1, 'admin', 'admin', 'admin', 'admin@example.com')
    get_users()