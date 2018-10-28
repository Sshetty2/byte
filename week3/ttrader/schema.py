import sqlite3

conn =  sqlite3.connect('ttrader.db')
cur = conn.cursor()


SQL = "DROP TABLE IF EXISTS accounts;"
cur.execute(SQL)

SQL = "DROP TABLE IF EXISTS trades;"
cur.execute(SQL)

SQL = "DROP TABLE IF EXISTS positions;"
cur.execute(SQL)


SQL = """
CREATE TABLE accounts(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR,
    pass_hash VARHAR (512),
    balance FLOAT,
    type VARHAR(3)
); """
cur.execute(SQL)

SQL = """
CREATE TABLE trades(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker VARCHAR,
    volume VARHAR,
    price FLOAT,
    account_pk INTEGER,
    time INTEGER,
	FOREIGN KEY(account_pk) REFERENCES accounts(pk)
); """

cur.execute(SQL)
SQL = """
CREATE TABLE positions(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker VARCHAR,
    amount VARHAR,
    account_pk INTEGER,
	FOREIGN KEY(account_pk) REFERENCES accounts(pk)
); """

cur.execute(SQL)


