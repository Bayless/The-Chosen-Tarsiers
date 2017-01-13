# Greetings, written by Rodda

import requests
import urllib, urllib2
import base64
import json
import spotify_db_manager
import time

last_fm_root = 'http://ws.audioscrobbler.com/2.0/'

def get_access_token():
    url = 'https://accounts.spotify.com/api/token'

    CLIENT_ID = open('utils/spotify_key').read().split('\n')[0]
    CLIENT_SECRET = open('utils/spotify_key').read().split('\n')[1]

    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}

    payload = {
        'grant_type': 'client_credentials'
    }

    data_encoded = urllib.urlencode(payload)
    
    r = urllib2.Request(url, data_encoded, headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

def authenticate():
    response = spotify_db_manager.get_current_access_token()

    if not response:
        token = get_access_token()
        spotify_db_manager.new_access_token(token['access_token'], time.time() + int(token['expires_in']))

    return spotify_db_manager.get_current_access_token()

# search_field should be a string of the search field
# type should be either album, artist, playlist, or track
def search(search_field = '', type='artist'):
    query_request = {'q' : search_field, 'type' : type}
    encoded = urllib.urlencode(query_request)

    url = 'https://api.spotify.com/v1/search?' + encoded

    headers = {"Authorization": "Bearer " + authenticate()}
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

def audio_features(id = ''):
    url = 'https://api.spotify.com/v1/audio-features/' + id
    print url

    headers = {"Authorization": "Bearer " + authenticate()}
    
    r = urllib2.Request(url, headers = headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

def get_top_artists(country = ''):
    url = last_fm_root

    api_key = open('utils/last_fm_key').read().split('\n')[1]

    query_request = {'method' : 'geo.gettopartists', 'country' : country, 'api_key' : api_key, 'format' : 'json'}
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    print url
    
    r = urllib2.Request(url)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

def get_similar(artist = '', track = ''):
    url = last_fm_root

    api_key = open('utils/last_fm_key').read().split('\n')[1]

    query_request = {'method' : 'track.getsimilar', 'artist' : artist, 'track': track,'api_key' : api_key, 'format' : 'json'}
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    print url
    
    r = urllib2.Request(url)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data


print get_similar('cher', 'believe')
