import sqlite3

def new_access_token(user,track,artist):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    new_access_token = 'INSERT INTO songs VALUES ("%s", "%s");' % (username, track, artist)
    c.execute(new_access_token)

    db.commit()
    db.close()

