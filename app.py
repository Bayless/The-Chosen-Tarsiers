# -*- coding: latin-1 -*-

from flask import Flask, render_template, request, redirect, url_for, session, flash
import time
import json
import random
import utils
from utils import accountManager, accounts_db_manager, helper, search
from utils import spotify

import config

app = Flask(__name__)

f = open( "utils/key", 'r' )

app.secret_key = f.read();
f.close

@app.route("/")
def loginOrRegister():
    if 'username' in session:
        return redirect("/map")
    else:
        return render_template("notLoggedIn.html")

@app.route("/authOrCreate", methods=["POST"])
def authOrCreate():
    formdict = request.form
    if formDict["logOrReg"] == "login":
        username = formDict["username"]
        password = formDict["password"]
        loginStatus = "login failed"
        statusNum = accountManager.authenticate(username,password) #returns 0,1 or 2 for login status messate
        if statusNum == 0:
            loginStatus = "user does not exist"
        elif statusNum == 1:
            session["username"]=username
            loginStatus = username + " logged in"
            return redirect( url_for("findSong") )
        elif statusNum == 2:
            loginStatus = "wrong password"
        return render_template("notLoggedIn.html",status=loginStatus)

    elif formDict["logOrReg"] == "register":
        username = formDict["username"]
        password = formDict["password"]
        pwd = formDict["pwd"]  #confirm password
        registerStatus = "register failed"
        statusNum = accountManager.register(username,password,pwd) #returns true or false
        if statusNum == 0:
            registerStatus = "username taken"
        elif statusNum == 1:
            registerStatus = "passwords do not match"
        elif statusNum == 2:
            registerStatus = username +" account created"
        elif statusNum == 3:
            registerStatus = "password too short"
        elif statusNum == 4:
            registerStatus = "username left blank"
        return render_template("notLoggedIn.html",status = registerStatus) #status is the login/creation messate
    else:
        return redirect(url_for("loginOrRegister"))


#logout of user
@app.route('/logout', methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop('username')
    return redirect(url_for('loginOrRegister'))

#ajax for saving songs
@app.route("/saveSong")
def saveSong():
    spotifyID = request.args.get("spotifyID")
    username = session['username']
    isSuccess = accounts_db_manager.saveSong(username,spotifyID)
    result = { "isSuccess": isSuccess}
    return json.dumps(result)

#ajax for removing saved  songs
@app.route("/removeSong")
def removeSong():
    spotifyID = request.args.get("spotifyID")
    username = session['username']
    isSuccess = accounts_db_manager.removeSong(username,spotifyID)
    result = { "isSuccess": isSuccess}
    return json.dumps(result)

@app.route("/mySongs")
def mySongs():
    if 'username' not in session:
        return redirect("/")
    #fake song list for testing
    user = session['username']
    #songs = accounts_db_manager.getMySongs(user)
    #fake song list for testing
    songs = [{"spotifyID":"spotify:track:2TpxZ7JUBn3uw46aR7qd6V","title":"Ma Cherie Amour","artist":"Stevie Wonder","country":"United States"},{"spotifyID":"1","title":"Golden Boy","artist":"Nadav Guedj","country":"Israel"}]

    songs = accounts_db_manager.getMySongs(user)
    return render_template("mysongs.html", songList = songs)

@app.route("/getSongAndInfo")
def getSongAndInfo():
    #here's a dictionary of available countries
    #now for getting the user-chosen country
    country = request.args.get("country")
    #get a song, its info, and another song and its info and put that into two dictionaries
    chosenSongInfo = {"countryCode":config.availableCountries[country],"countryName":country.upper(),"title":"","artist":""}
    #currently just getting a random country....  Song getting algo people, I will change this once you get me a song and its info
    randomCountry = random.choice(config.availableCountries.keys())
    #a list of dictionaries representing each of the 5 songs yeah
    #sorry the country thing is redundant
    generatedSongs = [
            {
                "countryCode":config.availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":config.availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":config.availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":config.availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":config.availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                }
            ]

    #put those two dictionaries together
    result = {'chosenSongInfo':chosenSongInfo,
            'generatedSongs':generatedSongs
            }

    return json.dumps(result)


@app.route("/map")
def findSong():
    if 'username' not in session:
        return redirect("/")
    else:
        return render_template("findSong.html")

#search results
@app.route('/searchResults', methods=["POST", "GET"])
def searchResults():
    if 'username' not in session:
        return redirect("/")
    else:
        formdict = request.form
        results = {}
        results = search.search(formdict["query"])
        #print "stuff: " + formdict['query']
        return render_template("searchResults.html", songList=results)

#returns basic song info
def getBasicInfo(id):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    info = { "spotifyID" : id,
                    "title": track,
                    "artist": artist}
    return info
#search results
@app.route('/searchedSong', methods=["POST", "GET"])
def searchedSong():
    if 'username' not in session:
        return redirect("/")
    spotifyID = request.args.get("spotifyID")
    givenSong = getBasicInfo(spotifyID)
    #title = request.args.get("title")
    #artist = request.args.get("artist")
    return render_template("searchedSong.html",givenSong=givenSong)

#About page
@app.route("/about")
def about():
    if 'username' not in session:
        return redirect("/")
    else:
        return render_template("about.html")

# Just in case...
@app.errorhandler(404)
def page_not_found(e):
    return render_template('nope.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('nope.html'), 500

if __name__ == "__main__":
    app.debug = True
    app.run()
