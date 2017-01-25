import sqlite3
from utils import spotify
import json

def saveSong(user,spotifyID):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

#check if already user already saved song
    c.execute('SELECT * FROM songs WHERE username = "%s" and songID = "%s";' % (user, spotifyID))
    result = c.fetchone()
    print result
    if result != None:
        return False

    new_access_token = 'INSERT INTO songs VALUES ("%s", "%s");' % (user, spotifyID)
    c.execute(new_access_token)

    db.commit()
    db.close()
    return True

#helper function
def getBasicInfo(id):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    info = { "spotifyID" : id,
        "title": track,
        "artist": artist}
    return info

def getMySongs(user):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    tupleSongs = 'SELECT * FROM songs WHERE username == "%s";' % (user)
    c.execute(tupleSongs)

    songList = [] #dis gon be your songs!
    out = c.fetchall()
    for song in out:
        songList.append(getBasicInfo(song[1]))
    print songList
    db.commit()
    db.close()

    return songList

def removeSong(user,spotifyID):
    f = 'database.db'
    db = sqlite3.connect(f)

    c = db.cursor()

    delete = 'DELETE FROM songs WHERE username == "%s" AND songID == "%s";' % (user,spotifyID)
    c.execute(delete)
    db.commit()
    db.close()

    return True



