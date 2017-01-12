from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")


@app.route("/loginRegister")
def notLoggedIn():
        return render_template("notLoggedIn.html")

@app.route("/map")
def mapTester():
        return render_template("findSong.html")

@app.route("/auto")
def autoTester():
        return render_template("autocompleteTester.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
