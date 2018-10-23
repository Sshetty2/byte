from sqlite3 import connect
from werkzeug import generate_password_hash, check_password_hash

connection = connect("ttrader.db")
cursor = connection.cursor()


def validate(username, password):
    SQL = "SELECT pk, password FROM users WHERE username=?;"
    cursor.execute(SQL, (username, ))
    row = cursor.fetchone()

    if not row:
        return None

    pk = row[0]
    pwhash = row[1]

    if not check_password_hash(pwhash, password):
        return None

    return pk


def createuser(username, password):
    SQL = "SELECT pk FROM users WHERE username=?;"
    cursor.execute(SQL, (username, ))
    row = cursor.fetchone()

    if row:
        raise KeyError("Username exists")

    SQL = "INSERT INTO users(username, password, balance) VALUES(?, ?, ?);"
    pwhash = generate_password_hash(password)
    cursor.execute(SQL, (username, pwhash, 0.0))
    connection.commit()


def updatepassword(username, currentpass, newpass):
    pk = validate(username, currentpass)
    if not pk:
        raise KeyError("Failed to validate")

    pwhash = generate_password_hash(newpass)
    SQL = "UPDATE users SET password = ? WHERE pk = ?;"
    cursor.execute(SQL, (pwhash, pk))
    connection.commit()


def getbalance(pk):
    SQL = "SELECT balance FROM users WHERE pk = ?;"
    cursor.execute(SQL, (pk, ))
    row = cursor.fetchone()
    if not row:
        raise KeyError("User does not exist")
    return row[0]


def getall():
    SQL = "SELECT pk, username FROM users ORDER BY username ASC;"
    cursor.execute(SQL)
    rows = cursor.fetchall()
    result = [{"username": row[1], "pk": row[0]} for row in rows]
    return result


def remove(pk):
    SQL = "DELETE FROM users WHERE pk = ?;"
    cursor.execute(SQL, (pk, ))
    connection.commit()


def cleanup():
    connection.close()
