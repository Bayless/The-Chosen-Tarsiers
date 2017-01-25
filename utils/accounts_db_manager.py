import sqlite3

def saveSong(user,spotifyID):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

#check if already user already saved song
    c.execute('SELECT * FROM songs WHERE access_token = "%s" and time = "%s";' % (user, spotifyID))
    result = c.fetchone()
    print result
    if result != None:
        return False

    new_access_token = 'INSERT INTO songs VALUES ("%s", "%s");' % (user, spotifyID)
    c.execute(new_access_token)

    db.commit()
    db.close()
    return True

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

    
