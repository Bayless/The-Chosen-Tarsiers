import utils
from utils import spotify
from utils import spotify_db_manager
from utils import music_graph
from utils import helper
import requests
import urllib, urllib2
import base64
import json
import time
import random

def getArtistRaw(country=""):
    raw = music_graph.search(country = country)["data"]
    return random.choice(raw)

def getArtistName(artistRaw):
    return artistRaw["name"]

def getArtistGenre(artistRaw):
    return artistRaw["main_genre"]

def getArtistID(artistRaw):
    return artistRaw["id"]

def getTrackRaw(artistID = ""):
    raw = music_graph.get_tracks(id = artistID)["data"]
    return random.choice(raw)

def getTrackAudio(trackID = ""):
    print spotify.audio_features(id = trackID)
        
# Need to store get
def getNewArtists(genre = "", country = ""):
    similarArtists = music_graph.search(country = country,limit = 10,genre = genre)
    
    return similarArtists

def getArtistMeta(country = ""):

# When given a dictionary of artist IDs, it will return a list of spotify IDs in the following format
# { artist: "[]", track: "[]", acoustiness: "[]".... }
# After given this list of spotifyIDs 
def getUberTracks(artist = []):

#return top 5 ids
def compareTracks(origID = "", comparableIDs = [], comparableAttributes)
    

# Function takes in a country, returns dictionary with artist name, artist ID, track, track ID, and spotify attributes
def geoAttributes(country = ""):
    raw = getArtistRaw(country)
    genre = getArtistGenre(raw) #store the genre somehow? 
    artistName = getArtistName(raw)
    artistID = getArtistID(raw)
    #potential issue is when there is no spotifyID
    raw = getTrackRaw(artistID)
    while (raw.isNull("spotify_track_id")):
        raw = getTrackRaw(artistID)
    trackName = raw["title"]
    trackID = raw["id"]
    spotifyTrackID = raw["spotify_track_id"]
    attributes = getTrackAudio(spotify_track_id)
    
    #get the spotify ID / some tracks will not have the spotify ID / do a bypass of this until the end of the project

    print trackName
    country = { "artist" : artistName,
             "artistID" : artistID,
             "track": trackName,
             "trackID": trackID,
             "spotifyID": " ",
             "genre" : genre}
    

print geoAttributes("France")

def trackInfo(id = ""):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    return { "spotifyID" : id,
             "title": track,
             "artist": artist}

#print trackInfo(id ="41ETKVJbZDSjATzW2wAqmc")

    
   
