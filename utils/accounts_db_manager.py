import sqlite3

def saveSong(user,spotifyID):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    new_access_token = 'INSERT INTO songs VALUES ("%s", "%s");' % (user, sopitfyID)
    c.execute(new_access_token)

    db.commit()
    db.close()

def getMySongs(user):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    tupleSongs = 'SELECT * FROM songs WHERE user == "%s";' % (user)
    p = c.execute(tupleSongs)
    for ID in p:
            info = spotify.tracks(ID)
            #go thru json file and get artist and track name
            #get lastfm stuff to get country

    db.commit()
    db.close()

    
