#!/usr/bin/env python3

import sqlite3

import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../datastores/master.db")

CONFIG = {
    'DBNAME': db_path,
}

DBNAME = "master.db"

## REST API ENDPOINT FUNCTION CALLS ##


def return_pass_hash(username):
    new_account_obj = Account(username=username)
    account_obj = new_account_obj.set_from_username()
    return account_obj.pass_hash

def validate_pw(userid, password):
    user_object = set_user_object(userid)
    if user_object.check_password(user_object.pass_hash, password):
        return True
    return False

##TODO:
def show_all_tweets(username):
    pass




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

    #def getposition(self, pk):

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

    def calculatehash(self, password):
        hashobject = hashlib.sha256()
        salt = CONFIG['SALT']
        saltedstring = password.encode() + salt.encode()
        hashobject.update(saltedstring)
        return hashobject.hexdigest()

    def check_password(self, hashed_password, user_password):
        hashobject = hashlib.sha256()
        salt = CONFIG['SALT']
        new_salted_string = user_password.encode() + salt.encode()
        hashobject.update(new_salted_string)
        new_hashed_pw = hashobject.hexdigest()
        if hashed_password == new_hashed_pw:
            return True
        return False

    def set_from_row(self, row):
        self.pk = row["pk"]
        self.username = row["username"]
        self.pass_hash = row["pass_hash"]
        self.number_of_tweets = row["number_of_tweets"]
        self.type = row["type"]
        return self

    ##TODO:
    def save_tweet(self, tweet):
        pass

    ##TODO:
    def delete_tweet(self, tweet):
        pass

    ##TODO:
    def update_tweet(self, tweet):
        pass
    

    def set_from_username(self):
        with OpenCursor() as cur: 
            SQL = """
            SELECT * FROM accounts WHERE username = ?;
            """
            cur.execute(SQL, (self.username, ))
            row=cur.fetchone()  
        self.set_from_row(row)
        return self