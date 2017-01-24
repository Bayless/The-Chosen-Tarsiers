# Greetings, written by Rodda

import requests
import urllib, urllib2
import base64
import json
import spotify_db_manager
import time
import api_manager

last_fm_root = 'http://ws.audioscrobbler.com/2.0/'

# Similar to search, it's the same, the url is different
def get_similar(artist = '', track = ''):
    url = last_fm_root

    api_key = open('utils/last_fm_key').read().split('\n')[1]

    query_request = {'method' : 'track.getsimilar', 'artist' : artist, 'track': track,'api_key' : api_key, 'format' : 'json'}
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)

# Return top artists, by country name [ISO 3166-1 country names]
def get_top_artists(country = ''):
    url = last_fm_root

    api_key = open('utils/last_fm_key').read().split('\n')[1]

    query_request = {'method' : 'geo.getTopArtists', 'country' : country, 'api_key' : api_key, 'format' : 'json'}

    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    print url
    
    r = urllib2.Request(url)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

# Return top artists, by country name [ISO 3166-1 country names]
def get_top_tracks(country = ''):
    url = last_fm_root

    api_key = open('utils/last_fm_key').read().split('\n')[1]

    query_request = {'method' : 'geo.getTopTracks', 'country' : country, 'api_key' : api_key, 'format' : 'json'}
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return issue_request(url)
