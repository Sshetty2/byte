import sqlite3


connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()

SQL_find_user = """
SELECT * FROM users WHERE username = ?;
"""

SQL_set_user = """
INSERT INTO users(username, pass_hash) VALUES(?,?);
"""

def find_insert_user(username, hashed_pw):
    cursor.execute(SQL_find_user, (username, ))
    row=cursor.fetchone()
    if not row:
        cursor.execute(SQL_set_user, (username, hashed_pw))
        print('user created')
    else:
        print('user exists')
    connection.commit()
    cursor.close()
    connection.close()

find_insert_user('sshetty', 565242526)


        