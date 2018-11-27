import sqlite3

CON = None
CUR = None


def setup(dbname="master.db"):
    global CON
    global CUR
    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

def run():
    SQL = "DROP TABLE IF EXISTS users;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR,
        pass_hash VARCHAR(128),
        type VARCHAR,
        number_of_tweets INTEGER;"""
    
    CUR.execute(SQL)
    
    SQL = "DROP TABLE IF EXISTS tweets;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE tweets(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        users_pk INTEGER,
        time INTEGER,
        FOREIGN KEY(users_pk) REFERENCES users(pk)
        );"""
    
    CUR.execute(SQL)
    
    SQL = "DROP TABLE IF EXISTS positions;"
    
    CUR.execute(SQL)
    
    SQL = """CREATE TABLE positions(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        account_pk INTEGER,
        ticker VARCHAR,
        amount INTEGER,
        FOREIGN KEY(account_pk) REFERENCES accounts(pk)
        );"""
    
    CUR.execute(SQL)
    
    CON.commit()
    CUR.close()
    CON.close()

if __name__ == "__main__":
    setup()
    run()
