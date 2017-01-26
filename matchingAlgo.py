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
import config

# When given a country, return a random artist
def getArtistRaw(country=''):
    raw = music_graph.search(country = country)['data']
    return raw

#When given JSON of random artist, return name
def getArtistName(artistRaw):
    return artistRaw['name']

#When given JSON of random artist, return name
def getArtistGenre(artistRaw):
    return artistRaw['main_genre']

#When givne JSON of random artist, return ID
def getArtistID(artistRaw):
    return artistRaw['id']

#When given an artist ID, return a random track
def getTrackRaw(artistID = ''):
    raw = music_graph.get_tracks(id = artistID)['data']
    return raw

#When given a spotify track ID, return spotify audio features
def getTrackAudio(trackID = ''):
    return spotify.audio_features(id = trackID)

# When given a country, return a song from country with spotify attributes
def geoAttributes(country = ''):
    raw = getArtistRaw(country)
    artist = random.choice(raw)
    while 'main_genre' not in artist:
        artist = random.choice(raw)
    genre = artist['main_genre']
    artistName = getArtistName(artist)
    artistID = getArtistID(artist)
    raw = getTrackRaw(artistID)
    track = raw[0]
    i = 0
    while (not('track_spotify_id' in track)):
        i += 1
        if i == len(raw):
            return 'NO SONGS FOUNDS'
        track = raw[i]
    trackName = track['title']
    trackID = track['id']
    spotifyTrackID = track['track_spotify_id']
    attributes = getTrackAudio(spotifyTrackID)
    energy = attributes['energy']
    danceability = attributes['danceability']
    instrumentalness = attributes['instrumentalness']
    acousticness = attributes['acousticness']

    return { 'country' : country,
             'artist' : artistName,
             'artistID' : artistID,
             'title': trackName,
             'trackID': trackID,
             'spotifyID': spotifyTrackID,
             'genre' : genre,
             'energy' : energy,
             'danceability' : danceability,
             'instrumentalness' : instrumentalness,
             'acousticness' : acousticness}


global generatedCountry
generatedCountry = ''
# When given a genre and country, return a dictionary of artists in genre with spotify id
def getNewArtists(genre = '', country = ''):
    randCountry = helper.getCountryNot(country)
    raw = music_graph.search(country = randCountry, limit = 65, genre = genre)    
    while (not raw['data']):
        randCountry = helper.getCountryNot(country)
        raw = music_graph.search(country = randCountry, limit = 65, genre = genre)
    global generatedCountry
    generatedCountry = randCountry
    returnDict = {}
    for artist in raw['data']:
        artistName = artist['name']
        if ('spotify_id' in artist):
            artistSpotifyID = artist['spotify_id']
            returnDict[artistName] = artistSpotifyID
        else:
            continue
    return returnDict

#When given spotify Artist ID, return list of dictionaries of top tracks from artist
def getTopTracks(spotifyArtistID = ''):
    list = []
    for track in spotify.get_top_tracks(id = spotifyArtistID, country = 'US')['tracks']:
        title = track['name']
        id = track['id']
        artist = track['artists'][0]['name']
        retDict =  { 'title': title,
                     'spotifyID' : id,
                     'artist' : artist,
                     'countryName' : generatedCountry,
                     'countryCode':  config.availableCountries[generatedCountry]
                     }
        list += [retDict]
    return list
    
# return list of dictionary of 5 songs
def similarTrackCompiler(genre = '', country = ''):
    newArtists = getNewArtists(genre = genre, country = country)
    i = 0 
    retDict = []
    for artist in newArtists:
        for track in getTopTracks(newArtists[artist]):
            i += 1
            retDict += [track]
            if i >= 5:
                return retDict
    return 'Not enough songs'

#When given a spotify song ID, return title and artist
def trackInfo(id = ''):
    raw = spotify.track(id)
    artist = raw['artists'][0]['name']
    track =  raw['name']
    return { 'spotifyID' : id,
             'title': track,
             'artist': artist
             }

def getNewArtistsFixedCountry(genre = '', country = ''):
    raw = music_graph.search(country = country, limit = 100, genre = genre)    
    global generatedCountry
    generatedCountry = country
    returnDict = {}
    for artist in raw['data']:
        artistSpotifyID = '-1'
        artistName = artist['name']
        if ('spotify_id' in artist):
            artistSpotifyID = artist['spotify_id']
        returnDict[artistName] = artistSpotifyID
    return returnDict

# return list of dictionary of 5 songs
def trackCompilerFixedCountry(id = '', country = ''):
    track = trackInfo(id)['artist']                                                                                                         
    genre = music_graph.getArtist(track)['data'][0]['main_genre']  
    newArtists = getNewArtistsFixedCountry(genre = genre, country = country)
    i = 0 
    retDict = []
    for artist in newArtists:
        for track in getTopTracks(newArtists[artist]):
            i += 1
            retDict += [track]
            if i >= 5:

                return retDict
    return 'Not enough songs'

def fixedCountrySimilar(id = '', country = ''):
    spotifyInfo = trackInfo(id)['artist']
    genre =  music_graph.getArtist(test)['data'][0]['main_genre']


#When given SpotifyID and country, return 5 similar songs from new country
