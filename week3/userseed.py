from sqlite3 import connect
from werkzeug import generate_password_hash

connection = connect("ttrader.db")
cursor = connection.cursor()

SQL = "DROP TABLE IF EXISTS users;"

cursor.execute(SQL)

SQL = """
CREATE TABLE users(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR,
    password VARCHAR,
    balance FLOAT
);"""

cursor.execute(SQL)

SQL = """
INSERT INTO users(username, password, balance) VALUES (?, ?, ?);
"""

pwcarter = generate_password_hash("password")
pwkenso = generate_password_hash("12345")

cursor.execute(SQL, ('carter', pwcarter, 3.50))
cursor.execute(SQL, ('kenso', pwkenso, 1000.00))

connection.commit()
connection.close()
