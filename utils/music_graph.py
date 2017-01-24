# Greetings, written by Rodda
import requests
import urllib, urllib2
import base64
import json
import spotify_db_manager
import time
import api_manager

music_graph_root = "http://api.musicgraph.com/api/v2/artist/"

# Similar to search, it's the same, the url is different
def search(name = '', country = 'Brazil'):
    url = music_graph_root + 'search'

    api_key = open('utils/music_graph_key').read().split('\n')[0]

    query_request = { 
                     'name' : name, 
                     'country' : country,
                     'api_key' : api_key, 
                     'limit': 5,
                     'format' : 'json'}

    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)

print search('Nicki Minaj', country = 'United States')

def get_info(id = ''):
    url = music_graph_root + id

    api_key = open('utils/music_graph_key').read().split('\n')[0]

    query_request = { 
        'api_key' : api_key, 
        'format' : 'json'
    }

    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)

def get_tracks(id = ''):
    url = music_graph_root + id + '/tracks'

    api_key = open('utils/music_graph_key').read().split('\n')[0]

    query_request = { 
        'api_key' : api_key, 
        'format' : 'json'
    }

    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)
