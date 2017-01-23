# -*- coding: latin-1 -*-

from flask import Flask, render_template, request, redirect, url_for, session, flash
import time
import json
import random
import utils
from utils import accountManager, accounts_db_manager

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
    formDict = request.form
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
    accounts_db_manager.saveSong(username,spotifyID)
    isSuccess = True #HARD CODED FOR NOW
    result = { "isSuccess": isSuccess}
    return json.dumps(result)

#hard-coded for now
@app.route("/mySongs")
def mySongs():
    if 'username' not in session:
        return redirect("/")
    else:
        #fake song list for testing
        user = session['username']
        #songs = accounts_db_manager.getMySongs(user)
        #fake song list for testing
        songs = [{"spotifyID":"spotify:track:2TpxZ7JUBn3uw46aR7qd6V","title":"Ma Cherie Amour","artist":"Stevie Wonder","country":"United States"},{"spotifyID":"1","title":"Golden Boy","artist":"Nadav Guedj","country":"Israel"}]
        return render_template("mySongs.html", songList = songs)

@app.route("/getSongAndInfo")
def getSongAndInfo():
    #here's a dictionary of available countries
    availableCountries = {"Bangladesh":"BD","Belgium":"BE","Burkina Faso":"BF","Bulgaria":"BG","Bosnia and Herz.":"BA","Brunei":"BN","Bolivia":"BO","Japan":"JP","Burundi":"BI","Benin":"BJ","Bhutan":"BT","Jamaica":"JM","Botswana":"BW","Brazil":"BR","Bahamas":"BS","Belarus":"BY","Belize":"BZ","Russia":"RU","Rwanda":"RW","Serbia":"RS","Timor-Leste":"TL","Turkmenistan":"TM","Tajikistan":"TJ","Romania":"RO","Guinea-Bissau":"GW","Guatemala":"GT","Greece":"GR","Eq. Guinea":"GQ","Guyana":"GY","Georgia":"GE","United Kingdom":"GB","Gabon":"GA","Guinea":"GN","Gambia":"GM","Greenland":"GL","Ghana":"GH","Oman":"OM","Tunisia":"TN","Jordan":"JO","Croatia":"HR","Haiti":"HT","Hungary":"HU","Honduras":"HN","Puerto Rico":"PR","Palestine":"PS","Portugal":"PT","Paraguay":"PY","Panama":"PA","Papua New Guinea":"PG","Peru":"PE","Pakistan":"PK","Philippines":"PH","Poland":"PL","Zambia":"ZM","W. Sahara":"EH","Estonia":"EE","Egypt":"EG","South Africa":"ZA","Ecuador":"EC","Italy":"IT","Vietnam":"VN","Solomon Is.":"SB","Ethiopia":"ET","Somalia":"SO","Zimbabwe":"ZW","Spain":"ES","Eritrea":"ER","Montenegro":"ME","Moldova":"MD","Madagascar":"MG","Morocco":"MA","Uzbekistan":"UZ","Myanmar":"MM","Mali":"ML","Mongolia":"MN","Macedonia":"MK","Malawi":"MW","Mauritania":"MR","Uganda":"UG","Malaysia":"MY","Mexico":"MX","Israel":"IL","France":"FR","Somaliland":"XS","Finland":"FI","Fiji":"FJ","Falkland Is.":"FK","Nicaragua":"NI","Netherlands":"NL","Norway":"NO","Namibia":"NA","Vanuatu":"VU","New Caledonia":"NC","Niger":"NE","Nigeria":"NG","New Zealand":"NZ","Nepal":"NP","Kosovo":"XK","Côte d'Ivoire":"CI","Switzerland":"CH","Colombia":"CO","China":"CN","Cameroon":"CM","Chile":"CL","N. Cyprus":"XC","Canada":"CA","Congo":"CG","Central African Rep.":"CF","Dem. Rep. Congo":"CD","Czech Rep.":"CZ","Cyprus":"CY","Costa Rica":"CR","Cuba":"CU","Swaziland":"SZ","Syria":"SY","Kyrgyzstan":"KG","Kenya":"KE","S. Sudan":"SS","Suriname":"SR","Cambodia":"KH","El Salvador":"SV","Slovakia":"SK","Korea":"KR","Slovenia":"SI","Dem. Rep. Korea":"KP","Kuwait":"KW","Senegal":"SN","Sierra Leone":"SL","Kazakhstan":"KZ","Saudi Arabia":"SA","Sweden":"SE","Sudan":"SD","Dominican Rep.":"DO","Djibouti":"DJ","Denmark":"DK","Germany":"DE","Yemen":"YE","Algeria":"DZ","United States":"US","Uruguay":"UY","Lebanon":"LB","Lao PDR":"LA","Taiwan":"TW","Trinidad and Tobago":"TT","Turkey":"TR","Sri Lanka":"LK","Latvia":"LV","Lithuania":"LT","Luxembourg":"LU","Liberia":"LR","Lesotho":"LS","Thailand":"TH","Fr. S. Antarctic Lands":"TF","Togo":"TG","Chad":"TD","Libya":"LY","United Arab Emirates":"AE","Venezuela":"VE","Afghanistan":"AF","Iraq":"IQ","Iceland":"IS","Iran":"IR","Armenia":"AM","Albania":"AL","Angola":"AO","Argentina":"AR","Australia":"AU","Austria":"AT","India":"IN","Tanzania":"TZ","Azerbaijan":"AZ","Ireland":"IE","Indonesia":"ID","Ukraine":"UA","Qatar":"QA","Mozambique":"MZ"}
    #now for getting the user-chosen country
    country = request.args.get("country")
    #get a song, its info, and another song and its info and put that into two dictionaries
    chosenSongInfo = {"countryCode":availableCountries[country],"countryName":country.upper(),"title":"","artist":""}
    #ASDFKJLASDJFASLDKFAA LOOK HERE !!!---------!!!!!!!!!!!!!!!KL:FDKFASD:FLKSAD:FK!!!!!
    #currently just getting a random country....  Song getting algo people, I will change this once you get me a song and its info
    randomCountry = random.choice(availableCountries.keys())
    #a list of dictionaries representing each of the 5 songs yeah
    #sorry the country thing is redundant
    generatedSongs = [
            {
                "countryCode":availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":availableCountries[randomCountry],
                "countryName":randomCountry,
                "title":"",
                "artist":"",
                "spotifyID":""
                },
            {
                "countryCode":availableCountries[randomCountry],
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
