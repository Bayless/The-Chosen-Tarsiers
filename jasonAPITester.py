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
    return raw

def getTrackAudio(trackID = ""):
    return spotify.audio_features(id = trackID)
        

# Function takes in a country, returns dictionary with artist name, artist ID, track, track ID, and spotify attributes
def geoAttributes(country = ""):
    raw = getArtistRaw(country)
    genre = getArtistGenre(raw) #store the genre somehow? 
    artistName = getArtistName(raw)
    artistID = getArtistID(raw)
    #potential issue is when there is no spotifyID
    raw = getTrackRaw(artistID)
    track = raw[0]
    i = 0
    while (not("track_spotify_id" in track)):
        i += 1
        track = raw[i]
    trackName = track["title"]
    trackID = track["id"]
    spotifyTrackID = track["track_spotify_id"]
    attributes = getTrackAudio(spotifyTrackID)
    energy = attributes["energy"]
    danceability = attributes["danceability"]
    instrumentalness = attributes["instrumentalness"]
    acousticness = attributes["acousticness"]
    #get the spotify ID / some tracks will not have the spotify ID / do a bypass of this until the end of the project

    return { "country" : country,
             "artist" : artistName,
             "artistID" : artistID,
             "track": trackName,
             "trackID": trackID,
             "spotifyID": spotifyTrackID,
             "genre" : genre,
             "energy" : energy,
             "danceability" : danceability,
             "instrumentalness" : instrumentalness,
             "acousticness" : acousticness}
    
test1 =  geoAttributes("France")

# Need to store get

def getNewArtists(genre = "", country = ""):
    randCountry = helper.getCountryNot(country)
    raw = music_graph.search(country = randCountry, limit = 10, genre = genre)    

    while (not raw["data"]):
        randCountry = helper.getCountryNot(country)
        raw = music_graph.search(country = randCountry, limit = 10, genre = genre)    

    returnDict = {}
    for artist in raw["data"]:
        artistSpotifyID = "-1"
        artistName = artist["name"]
        if ("spotify_id" in artist):
            artistSpotifyID = artist["spotify_id"]
        returnDict[artistName] = artistSpotifyID
    return returnDict

#similarArtist1 =  getNewArtists(genre = test1["genre"], country = test1["country"])

#similarArtist1ID = similarArtist1[random.choice(similarArtist1.keys())]

#print similarArtist1ID

foo = "1CdMxozoRr9f9kew8DMjKg"

def getTopTracks(spotifyArtistID = ""):
    return spotify.get_top_tracks(spotifyArtistID)

print getTopTracks(foo)

#print trackInfo(id ="41ETKVJbZDSjATzW2wAqmc")
   
def trackInfo(id = ""):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    return { "spotifyID" : id,
             "title": track,
             "artist": artist}

