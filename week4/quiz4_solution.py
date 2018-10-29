import sqlite3
import hashlib
import uuid

connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()

SQL_find_user = """
SELECT * FROM users WHERE username = ?;
"""

SQL_set_user = """
INSERT INTO users(username, pass_hash) VALUES(?,?);
"""

def calculatehash(password):
    hashobject = hashlib.sha256()
    salt = uuid.uuid4().hex
    saltedstring = password.encode() + salt.encode()
    hashobject.update(saltedstring)
    return hashobject.hexdigest() + ':' + salt


def find_insert_user(username, password):
    hashed_pw = calculatehash(password)
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

        