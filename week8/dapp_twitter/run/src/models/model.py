#!/usr/bin/env python3

import sqlite3

import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../datastores/master.db")

CONFIG = {
    'DBNAME': db_path,
}

DBNAME = "master.db"


class OpenCursor:
    def __init__(self, *args, **kwargs):
        # update:
        if 'dbname' in kwargs:
            self.dbname = kwargs['dbname']
            del(kwargs['dbname'])
        else:
            self.dbname = CONFIG['DBNAME']

        self.conn = sqlite3.connect(self.dbname, *args, **kwargs)
        self.conn.row_factory = sqlite3.Row  # access fetch results by col name
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, extype, exvalue, extraceback):
        if not extype:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()


class Account:
    def __init__(self, pk=None, username=None, pass_hash=None, user_type= None, number_of_tweets=None):
        self.pk = pk
        self.username = username
        self.pass_hash = pass_hash
        self.type = user_type
        self.number_of_tweets = number_of_tweets

    def save(self):
        with OpenCursor() as cur:
            if not self.pk:
                SQL = """
                INSERT INTO accounts(username, pass_hash, type, number_of_tweets)
                VALUES(?, ?, ?, ?);
                """
                cur.execute(SQL, (self.username, self.pass_hash, self.user_type, self.number_of_tweets))
                self.pk = cur.lastrowid

            else:
                SQL = """
                UPDATE accounts SET username=?, pass_hash=?, type=?, number_of_tweets=? WHERE
                pk=?;
                """
                cur.execute(SQL, (self.username, self.pass_hash, self.type,
                                  self.number_of_tweets))
    
    def write_tweet(self):
        pass

    def __repr__(self):
        display ="Account PK = {}, Username = {}, PW Hash = {}, Balance = {}".format(self.pk, self.username, self.pass_hash, self.balance)
        return display

    def set_from_row(self, row):
        self.pk = row["pk"]
        self.username = row["username"]
        self.pass_hash = row["pass_hash"]
        self.number_of_tweets = row["number_of_tweets"]
        self.type = row["type"]
        return self