import sqlite3
from time import time
import werkzeug

conn = sqlite3.connect("ttrader.db")
cur = conn.cursor()

SQL = """INSERT INTO accounts(username, pass_hash, balance, type)
VALUES(?, ?, ?, ?);"""
pw_hash = werkzeug.generate_password_hash("password")
cur.execute(SQL, ("carter", pw_hash, 10000.0, 'USER'))

SQL = """INSERT INTO trades(account_pk, ticker, volume, price, time) 
VALUES(?, ?, ?, ?, ?);"""
cur.execute(SQL, (1, "AAPL", 10, 100.0, int(time())))

SQL = """INSERT INTO positions(account_pk, ticker, amount) VALUES(?, ?, ?);"""
cur.execute(SQL, (1, "AAPL", 10))

conn.commit()
cur.close()
conn.close()
