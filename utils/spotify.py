# Greetings, written by Rodda

import requests
import urllib, urllib2
import base64
import json

# search_field should be a string of the search field
# type should be either album, artist, playlist, or track
def search(search_field = '', type='artist'):
    query_request = {'q' : search_field, 'type' : type}
    encoded = urllib.urlencode(query_request)
    
    url = 'https://accounts.spotify.com/api/token'

    CLIENT_ID = open('spotify_key').read().split('\n')[0]
    CLIENT_SECRET = open('spotify_key').read().split('\n')[1]

    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}

    payload = {
        'grant_type': 'client_credentials'
    }

    data_encoded = urllib.urlencode(payload)
    
    r = urllib2.Request(url, data_encoded, headers)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    print response_data


search('hi')
    
