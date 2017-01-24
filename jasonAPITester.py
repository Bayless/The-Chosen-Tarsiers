from flask import Flask, render_template, request, redirect, url_for, session, flash
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

def match_last(artist="",track="",number = 5):
    raw =  last_fm.get_similar(artist,track)
    for i in range(0,5):
        track =  raw['similartracks']["track"][i]['name']
        singer = raw['similartracks']["track"][i]['artist']["name"]
        print track + " : " + singer
    
def get_top_artists(country=""):
    raw =  last_fm.get_top_artists(country)
    for i in range(0,5):
        artist =  raw['topartists']["artist"][i]['name']
        print artist


def get_top_tracks(country=""):
    raw =  last_fm.get_top_tracks(country)
    track =  raw['tracks']["track"][0]['name']
    spot =  spotify.search(search_field = track, type = "track")
    uri = spot['tracks']['items']
    print uri
    returnDict = { track: track,
                   uri: uri,
                   artist: artist}
    artist =  raw['tracks']["track"][0]['artist']['name']
    return returnDict

def countrySearch(country=""):
   dict = get_top_tracks(country)
   track = dict['track']
   uri = dict['uri']
   artist = dict['artist']
   return track


def spotifyRecommend(id = ""):
    # need to parse through the audio features to get danceability, acoustiness, energy, instrumentalness
    raw = spotify.audio_features(id)
    dance = raw[0]
    acous = raw[1]
    energy = raw[2]
    instru = raw[3]

    
    # get random country to put into the rec algo to get 5 similar songs
    randomCountry = random.choice(availableCountries.keys())

    recs = spotify.get_recommendations(limit = 5,
                                market = randomCountry,
                                danceability = dance,
                                acousticness = acous,
                                energy = energy,
                                instrumentalness = instru,
                                seed_id = id)
    #need to parse through these recs to return dict

    return retDict

#artistGenre = ""

def getArtistGenre():
    print "BLOT"

def artistReturn(country= ""):
    artistRaw = music_graph.artist_country(country = country)["data"]
    artistID = artistRaw[0]["id"]
    artistGenre = artistRaw[0]["main_genre"]
    trackRaw = music_graph.get_tracks(id = artistID)["data"]

    for n in range(0, len(trackRaw)):
        if "track_spotify_id" in trackRaw[n]:
            return trackRaw[n]["track_spotify_id"]
        return "There is no Spotify ID"
    
#testID = artistReturn(country = "Israel")
    
def getAttributes(id = ""):
    print spotify.audio_features(id = id)
        
#getAttributes(id = testID)

#print "aristGenre: " + artistGenre

#randomCountry = helper.getCountryNot("Israel")

def getNewArtists(genre = "", country = ""):
    bleh = music_graph.search(country = country,limit = 10,genre = genre)

#print getNewArtists(genre = artistGenre, country = randomCountry)

def trackInfo(id = ""):
    raw = spotify.track(id)
    artist = raw["artists"][0]["name"]
    track =  raw["name"]
    return { "spotifyID" : id,
             "title": track,
             "artist": artist}

print trackInfo(id ="41ETKVJbZDSjATzW2wAqmc")

    
   
