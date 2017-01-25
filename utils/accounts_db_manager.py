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

def updateFullName(username, name):
    f = "database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    p = 'SELECT EXISTS(SELECT fullName FROM users WHERE username = "%s" LIMIT 1)'%(username)
    c.execute(p)
    if (c.fetchone()[0] == 0):
        oldName = "you had no previous name!"
    else:
        p = 'SELECT fullName FROM users WHERE username == "%s" '%(username)
        c.execute(p)
        oldName = c.fetchone()[0]

    p = 'UPDATE users SET fullName = "%s" WHERE username == "%s"'%(name, username)
    c.execute(p)

    db.commit()
    db.close()
    return oldName

def updateDob(username,birth):
    f = "database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    
    p = 'SELECT EXISTS(SELECT dob FROM users WHERE username = "%s" LIMIT 1)'%(username)
    c.execute(p)
    if (c.fetchone()[0] == 0):
        oldDob = "you had no previous birthdate!"
    else:
        p = 'SELECT dob FROM users WHERE username == "%s" '%(username)
        c.execute(p)
        oldDob = c.fetchone()[0]

    p = 'UPDATE users SET dob = "%s" WHERE username == "%s"'%(birth, username)
    c.execute(p)

    db.commit()
    db.close()
    return oldDob

def updatePwd(username,pwd):
    f = "database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    
    passHash = sha1(pwd).hexdigest()#hash it
    p = 'UPDATE users SET password = "%s" WHERE username == "%s"'%(passHash, username)

    c.execute(p)

    db.commit()
    db.close()

#gonna return just username and number_saved_songs
def get_user_info(user):
    f = "database.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    
    p = 'SELECT COUNT(username) FROM songs WHERE username == "%s"'%(user)

    c.execute(p)

    numSongs = c.fetchone()[0]

    return {"username":user,
            "number_saved_songs":numSongs}

    db.commit()
    db.close()
    



