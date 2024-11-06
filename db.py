# import sqlite3 as sql
#
# connection = sql.connect('database.db')
# cursor = connection.cursor()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Users(
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         age INTEGER
#     )
# ''')
#
# cursor.execute('''
#     CREATE INDEX IF NOT EXISTS idx_email ON Users (email)
# ''')

# for i in range(20):
#     cursor.execute(" INSERT INTO Users (username, email, age) VALUES(?,?,?)", (f'{i}newuser', f'{i}ex@gmail.com', i+10))

#  cursor.execute("UPDATE Users SET age = ? WHERE username = ?",  (999, 'newuser'))

# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser', ))

#SELECT FROM WHERE GROUP BY HAVING ORDER BY

# cursor.execute("SELECT username, age FROM Users WHERE age > ?", (20,))
#
# cursor.execute("SELECT age, AVG(age) FROM Users GROUP BY AGE ")
# users = cursor.fetchall()
# for user in users:
#     print(user)
#
# cursor.execute("SELECT SUM(age) FROM Users WHERE age % 3 == 0")
# x = cursor.fetchone()[0]
# print(x)
# connection.commit()
# connection.close()


import sqlite3 as sql

connection = sql.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INT,
        username TEXT,
        first_name TEXT,
        block INT
    );
''')


def add_user(user_id, user_name, first_name, ):
    check_user = cursor.execute("SELECT * FROM Users WHERE  id = ?", (user_id))
    if check_user.fetchone() is None:
        cursor.execute(f'''
            INSERT INTO Users VALUES ('{user_id}', '{user_name}', '{first_name}', 0)
        ''')
    connection.commit()


def show_users():
    users_list = cursor.execute("SELECT * FROM Users")
    message = ''
    for user in users_list:
        message = f'{user[0]} @{[user[1]]} {user[2]} \n'
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute("SELECT COUNT(*) FROM Users ").fetchone()
    connection.commit()
    return count_users


def add_to_block(id):
    cursor.execute(f'UPDATE Users SET block = ? WHERE id = ?', (1, id))
    connection.commit()


def remove_block(id):
    cursor.execute(f'UPDATE Users SET block = ? WHERE id = ?', (0, id))
    connection.commit()


def check_block(id):
    user = cursor.execute(f'SELECT block FROM Users WHERE id = ?', (id,)).fetchone()
    connection.commit()
    return user[0]


connection.commit()
connection.close()
