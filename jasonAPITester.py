import utils
from utils import spotify
from utils import spotify_db_manager
from utils import last_fm
from utils import music_graph
from utils import helper
import requests
import urllib, urllib2
import base64
import json
import time
import random

def getArtistRaw(country=""):
    return music_graph.artist_country(country = country)["data"]

def getArtistGenre(artistRaw):
    return artistRaw[0]["main_genre"]

def getArtistID(artistRaw):
    return artistRaw[0]["id"]

def getTrackRaw(artistID = ""):
    return music_graph.get_tracks(id = artistID)["data"]

def getAttributes(trackID = ""):
    print spotify.audio_features(id = trackID)
        
def getNewArtists(genre = "", country = ""):
    bleh = music_graph.search(country = country,limit = 10,genre = genre)

# Function takes in a country, returns dictionary with artist name, artist ID, track, track ID, and spotify attributes
def geoAttributes(country = ""):
    raw = getArtistRaw(country)
    genre = getArtistGenre(raw)
    artistID = getArtistID(raw)

    raw = getTrackRaw(artistID)
    print raw
    

print geoAttributes("France")

def trackInfo(id = ""):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    return { "spotifyID" : id,
             "title": track,
             "artist": artist}

#print trackInfo(id ="41ETKVJbZDSjATzW2wAqmc")

    
   
