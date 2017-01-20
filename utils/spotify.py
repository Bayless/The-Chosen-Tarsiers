# Greetings, written by Rodda

import requests
import urllib, urllib2
import base64
import json
import spotify_db_manager
import time

# get_access_token()
# Retrieves an access token from Spotify
def get_access_token():
    url = 'https://accounts.spotify.com/api/token' # base url
   
    CLIENT_ID = open('utils/spotify_key').read().split('\n')[0] # Getting the client id and secret from the spotify_key folder
    CLIENT_SECRET = open('utils/spotify_key').read().split('\n')[1]

    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET)) # Encodes it in base 64, as required by Spotify
    headers = {"Authorization": "Basic {}".format(base64encoded)} # Also required by Spotify

    payload = {
        'grant_type': 'client_credentials'
    }

    data_encoded = urllib.urlencode(payload) # Encodes the data
    
    r = urllib2.Request(url, data_encoded, headers) # Setups the object

    response = urllib2.urlopen(r, timeout = 30).read() # Executes the response
    response_data = json.loads(response) # Saves as a json
    
    return response_data

# authenticate()
# Gets the current access token from the db manager
def authenticate():
    response = spotify_db_manager.get_current_access_token()

    if not response: # If the current token is not valid
        token = get_access_token() # Get a new one
        spotify_db_manager.new_access_token(token['access_token'], time.time() + int(token['expires_in'])) # Saves it properly

    return spotify_db_manager.get_current_access_token() # Returns the current, which is guaranteed to be valid

def track(id = ''):
    url = 'https://api.spotify.com/v1/tracks/' + id

    headers = {"Authorization": "Bearer " + authenticate()} # Gets the current access token
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data # Issues response and receives it

# search_field should be a string of the search field
# type should be either album, artist, playlist, or track
def search(search_field = '', type='artist'):
    query_request = {'q' : search_field, 'type' : type} # query result
    encoded = urllib.urlencode(query_request) # Encodes the parameters

    url = 'https://api.spotify.com/v1/search?' + encoded # Base URL

    headers = {"Authorization": "Bearer " + authenticate()} # Gets the current access token
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data # Issues response and receives it

# Similar to search, it's the same, the url is different 
def audio_features(id = ''):
    url = 'https://api.spotify.com/v1/audio-features/' + id
    print url

    headers = {"Authorization": "Bearer " + authenticate()}
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data


# Similar to search, it's the same, the url is different
def get_recommendations(limit = 1, market = 'US',
                        max_danceability = 1.0, min_danceability = 0.0,
                        max_acousticness = 1.0, min_acousticness = 0.0,
                        max_energy = 1.0, min_energy = 0.0,
                        max_instrumentalness = 1.0, min_instrumentalness = 0.0,
                        seed_artists = '', seed_genres = '', seed_tracks = ''):

    query_request = {'limit' : limit, 
                     'max_danceability' : max_danceability,
                     'min_danceability' : min_danceability,
                     'max_acousticness' : max_acousticness,
                     'min_acousticness' : min_acousticness,
                     'max_energy' : max_energy,
                     'min_energy' : min_energy,
                     'max_instrumentalness' : max_instrumentalness,
                     'min_instrumentalness' : min_instrumentalness,
                     'seed_artists' : seed_artists, 'seed_genres' : seed_genres, 'seed_tracks': seed_tracks}

    encoded = urllib.urlencode(query_request)

    url = 'https://api.spotify.com/v1/recommendations?' + encoded

    headers = {"Authorization": "Bearer " + authenticate()}
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

print track('5t0E9V1RiHBflzs71pfGGG')
