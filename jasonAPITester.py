from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils
#from utils import spotify
#from utils import spotify_db_manager
from utils import last_fm
import requests
import urllib, urllib2
import base64
import json
import time


#print raw


def match_last(artist="",track="",number = 5):
    raw =  last_fm.get_similar(artist,track)
    for i in range(0,5):
        track =  raw['similartracks']["track"][i]['name']
        singer = raw['similartracks']["track"][i]['artist']["name"]
        print track + " : " + singer
    
#print match_last("the beatles","eleanor rigby")

def get_top_artists(country=""):
    raw =  last_fm.get_top_artists(country)
    for i in range(0,5):
        artist =  raw['topartists']["artist"][i]['name']
        print artist


#print get_top_artists("Israel")

def get_top_tracks(country=""):
    raw =  last_fm.get_top_tracks(country)
    for i in range(0,100):
        track =  raw['tracks']["track"][i]['name']
        print track
        artist =  raw['tracks']["track"][i]['artist']['name']
        print artist


print get_top_tracks("Uganda")

#print spotify.search("Bob Dylan")
