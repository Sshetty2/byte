#!/usr/bin/env python3

import sqlite3
import time
import hashlib
import uuid
from datetime import datetime
from pytz import timezone

fmt = '%H:%M:%S %m-%d-%Y'
eastern = timezone('US/Eastern')
naive_dt = datetime.now()
loc_dt = datetime.now(eastern)
date_now = naive_dt.strftime(fmt)




CON = None
CUR = None


def calculatehash(password):
    hashobject = hashlib.sha256()
    salt = "!$33gl3d33g"
    saltedstring = password.encode() + salt.encode()
    hashobject.update(saltedstring)
    return hashobject.hexdigest()


def setup(dbname="master.db"):
    global CON
    global CUR
    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()





def run():
    SQL = "DELETE FROM users;"
    CUR.execute(SQL)

    SQL = "DELETE FROM sqlite_sequence WHERE name = 'users';"
    CUR.execute(SQL)

    SQL = """INSERT INTO users(username, pass_hash, type)
    VALUES(?, ?, ?);"""
    pw_hash = calculatehash("password")
    CUR.execute(SQL, ("adam deMAN", pw_hash, 'USER'))
    CUR.execute(SQL, ("blake", pw_hash,'USER'))
    CUR.execute(SQL, ("ders", pw_hash, 'USER'))
    CUR.execute(SQL, ("NASA", pw_hash, 'USER'))
    CUR.execute(SQL, ("Proton Mail", pw_hash, 'USER'))
   
    SQL = "DELETE FROM tweets;"
    CUR.execute(SQL)

    SQL = "DELETE FROM sqlite_sequence WHERE name = 'tweets';"
    CUR.execute(SQL)

    SQL = """INSERT INTO tweets(users_pk, username, content, image_pathname, ipfs_hash, time) 
    VALUES(?, ?, ?, ?, ?, ?);"""
    CUR.execute(SQL, (1, "adam deMAN", "I tried out for the high school wrestling team and guess what?","uploads/adam.jpg", "QmURTo5e9f6zTDJVyhN91wjRxntjP99hwMZG3U9gp4DxHG", datetime.utcfromtimestamp(1544020873).strftime('%I:%M:%S %m-%d-%Y')))
    CUR.execute(SQL, (2, "blake", "braj","uploads/blake.jpg", "QmQLdT2XVTgfuAPt85e1mUMdArvJdKda5XQfL73sNjwLAa", datetime.utcfromtimestamp(1544020873).strftime('%I:%M:%S %m-%d-%Y')))
    CUR.execute(SQL, (3, "ders", "DANG, what's up wit' all deez books?","uploads/ders.jpg", "QmVpTYBsvk9q7MQDuz3i6hEU5dsESwnKeGP1B3XC1NSZwd", datetime.utcfromtimestamp(1544020873).strftime('%I:%M:%S %m-%d-%Y')))
    CUR.execute(SQL, (4, "NASA", "	Check out this photo. we took instead of the one we were going to take of our lunch","uploads/PIA22867-640x350.jpg", "QmZVZDvgQBWyBKKpHf34nYorkCNPiBM95drcTLyxYSBVL1", datetime.utcfromtimestamp(1544020873).strftime('%I:%M:%S %m-%d-%Y')))
    CUR.execute(SQL, (5, "Proton Mail", "Interested in system architecture? Here's how to implement end-to-end encryption at Proton Mail","uploads/Protonmail_system_architecture_2014.png", "QmdrzzfWQtLenS67Ke7qV2N1i9Tc1qhx5fiP2He4kx5z1E", datetime.utcfromtimestamp(1544020873).strftime('%I:%M:%S %m-%d-%Y')))

    CON.commit()
    CUR.close()
    CON.close()


if __name__ == "__main__":
    setup()
    run()
