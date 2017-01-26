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

def getArtist(name = ''):
    url = music_graph_root+"search"

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = { 
            'name' : name, 
            'api_key' : api_key, 
            'limit' : 1,
            'format' : 'json'}
    
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)



def search(name = '', country = '', genre = '', limit = 100):
    url = music_graph_root+"search"

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    if not genre == '':
        query_request = { 
            'name' : name, 
            'country' : country,
            'genre' : genre,
            'api_key' : api_key, 
            'limit': limit,
            'format' : 'json'}
    else:
        query_request = { 
            'name' : name, 
            'country' : country,
            'api_key' : api_key, 
            'limit': limit,
            'format' : 'json'}
    
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)


def get_similar_song_name(name = '', offset = 1):
    url = "http://api.musicgraph.com/api/v2/track/"
    url += 'suggest'

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = { 
        'prefix' : name, 
        'api_key' : api_key, 
        'limit': 20,
        'offset': offset,
        'format' : 'json'}
        
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)

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


def get_spotify_id(track_id = ''):
    url = "http://api.musicgraph.com/api/v2/track/"
    url += track_id

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = { 
        'api_key' : api_key, 
        'format' : 'json'}
        
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded
    return api_manager.issue_request(url)


def get_tracks(id = ''):
    url = music_graph_root + id + '/tracks'

    api_key = open('utils/music_graph_key').read().split('\n')[0]
    query_request = { 
        'api_key' : api_key, 
        'format' : 'json',
        'limit': 100
        }
    encoded = urllib.urlencode(query_request)

    url += '?' + encoded

    return api_manager.issue_request(url)
