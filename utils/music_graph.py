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

def artist_country(country=""):
    url = music_graph_root+"search"
    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = {                       
                     'country' : country,
                     'api_key' : api_key, 
                     'limit': 1,
                     'format' : 'json'}
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    print url
    
    r = urllib2.Request(url)

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data



def search(name = '', country = '', genre = ''):
    url = music_graph_root+"search"

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = { 
        'name' : name, 
        'country' : country,
        'genre' : genre,
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

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
    
    return response_data

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
