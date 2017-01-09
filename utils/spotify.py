# Greetings, written by Rodda

import requests
import urllib

# search_field should be a string of the search field
# type should be either album, artist, playlist, or track
def search(search_field = '', type='artist'):
    query_request = {'q' : search_field, 'type' : type}
    encoded = urllib.urlencode(query_request)
    url = 'https://api.spotify.com/v1/search?' + encoded

#    keys = 'Basic ' + open('spotify_key').read().split('\n')[0] + ':' + open('spotify_key').read().split('\n')[1]
#    print keys
#    headers = {'Authorization' : keys}

#    r = requests.get(url, headers = headers)

    r = requests.get(url)

    print r
    print r.headers
    print r.text

search('hi')
    
