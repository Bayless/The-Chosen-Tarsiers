import sqlite3
import time

def new_access_token(access_token, time):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    new_access_token = 'INSERT INTO spotify VALUES ("%s", %d);' % (access_token, time)
    c.execute(new_access_token)

    db.commit()
    db.close()

def get_current_access_token():
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    fetch = 'SELECT * FROM spotify'
    c.execute(fetch)
    response = c.fetchall()

    if response:
        for token in response:
            token_time = token[1]
            current_time = time.time()

            if token_time > current_time:
                return token[0]
    return False

    db.commit()
    db.close()
