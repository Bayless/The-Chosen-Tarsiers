from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route("/")
def loginOrRegister():
    if 'username' in session:
        return redirect("/map")
    else:
        return render_template("notLoggedIn.html", username=True, message=False)


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
            return redirect( "/profile" )
        elif statusNum == 2:
            loginStatus = "wrong password"

        return render_template("notLoggedIn.html",status=loginStatus, message=True)

    elif formDict["logOrReg"] == "register":  #registering
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

        return render_template("notLoggedIn.html",status=registerStatus, message=True) #status is the login/creation messate 
    else:
        return redirect(url_for("loginOrReg"))

#logout of user
@app.route('/logout', methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop('username')
    return redirect(url_for('loginOrRegister'))


@app.route("/map")
def mapTester():
        return render_template("mapTester.html")

if __name__ == "__main__":
    #app.debug = True                                                                                                        
    app.run()
