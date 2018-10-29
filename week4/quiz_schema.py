import sqlite3

CREATESQL = """
CREATE TABLE users(
pk INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR,
pass_hash VARCHAR(128)
);
"""

connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()
cursor.execute(CREATESQL)
cursor.close()
connection.close()
