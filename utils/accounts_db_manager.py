import sqlite3

def new_access_token(song, user):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    new_access_token = 'INSERT INTO songs VALUES ("%s", %d);' % (access_token, time)
    c.execute(new_access_token)

    db.commit()
    db.close()

