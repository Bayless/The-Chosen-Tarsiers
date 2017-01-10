from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import utils.master
import utils.ticketmaster
import utils.ticketleap
import utils.seatgeek

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    return render_template("output.html",events=eventList)

if __name__ == "__main__":
    app.debug = False
    app.run()
