from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils
from utils import spotify
from utils import spotify_db_manager
from utils import last_fm
from utils import music_graph
import requests
import urllib, urllib2
import base64
import json
import time


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


'''
So let me just think aout some stuff on this train so that when i am at Whole Foods, I won't be totally
lost as the where I wan to elad this project.

There are a few algoithrims that I need to work on

1. So here is how Spotify works:

I get a country from the random country map that is on the lef othe site 
I use the last.fm api to get a top track from that country [note that this track is not nec. from that country]
I use the spot acoustics api to get some attributes
I get another random country from a random country generator
I then take that country and find the relevant 2 letter code
I use the spotiify rec to get me a song that is popular in that maret and has similar attributes
to the orig rand song from the orig country that a person clicked on


2. Here is how MusicGraph might fix this + some musings

I get a country from the country map when clicked
I used MusicMatch to get a popular artist from that country
I use last.fm to get a popular song from that artist
I use the search api from spotify to get the track id for spotify
I keep this track id for the song of the artist from the country
I get the spotify acoustic attributes of that song
I generate a random country
a.I use MusicMatch to get me an artist from rand country that is similar to artist of orig country
b. I use musicMatch to get me a similar song [migt be jank]
c. I use Spotify to get me a song that similar to the orig song


'''

print music_graph.suggest(name="John Lennon", country = "Israel")
   
