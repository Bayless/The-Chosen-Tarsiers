# -*- coding: latin-1 -*-                                                                                         

availableCountries = {"Bangladesh":"BD","Belgium":"BE","Burkina Faso":"BF","Bulgaria":"BG","Bosnia and Herz.":"BA","Brunei":"BN","Bolivia":"BO","Japan":"JP","Burundi":"BI","Benin":"BJ","Bhutan":"BT","Jamaica":"JM","Botswana":"BW","Brazil":"BR","Bahamas":"BS","Belarus":"BY","Belize":"BZ","Russia":"RU","Rwanda":"RW","Serbia":"RS","Timor-Leste":"TL","Turkmenistan":"TM","Tajikistan":"TJ","Romania":"RO","Guinea-Bissau":"GW","Guatemala":"GT","Greece":"GR","Eq. Guinea":"GQ","Guyana":"GY","Georgia":"GE","United Kingdom":"GB","Gabon":"GA","Guinea":"GN","Gambia":"GM","Greenland":"GL","Ghana":"GH","Oman":"OM","Tunisia":"TN","Jordan":"JO","Croatia":"HR","Haiti":"HT","Hungary":"HU","Honduras":"HN","Puerto Rico":"PR","Palestine":"PS","Portugal":"PT","Paraguay":"PY","Panama":"PA","Papua New Guinea":"PG","Peru":"PE","Pakistan":"PK","Philippines":"PH","Poland":"PL","Zambia":"ZM","W. Sahara":"EH","Estonia":"EE","Egypt":"EG","South Africa":"ZA","Ecuador":"EC","Italy":"IT","Vietnam":"VN","Solomon Is.":"SB","Ethiopia":"ET","Somalia":"SO","Zimbabwe":"ZW","Spain":"ES","Eritrea":"ER","Montenegro":"ME","Moldova":"MD","Madagascar":"MG","Morocco":"MA","Uzbekistan":"UZ","Myanmar":"MM","Mali":"ML","Mongolia":"MN","Macedonia":"MK","Malawi":"MW","Mauritania":"MR","Uganda":"UG","Malaysia":"MY","Mexico":"MX","Israel":"IL","France":"FR","Somaliland":"XS","Finland":"FI","Fiji":"FJ","Falkland Is.":"FK","Nicaragua":"NI","Netherlands":"NL","Norway":"NO","Namibia":"NA","Vanuatu":"VU","New Caledonia":"NC","Niger":"NE","Nigeria":"NG","New Zealand":"NZ","Nepal":"NP","Kosovo":"XK","Côte d'Ivoire":"CI","Switzerland":"CH","Colombia":"CO","China":"CN","Cameroon":"CM","Chile":"CL","N. Cyprus":"XC","Canada":"CA","Congo":"CG","Central African Rep.":"CF","Dem. Rep. Congo":"CD","Czech Rep.":"CZ","Cyprus":"CY","Costa Rica":"CR","Cuba":"CU","Swaziland":"SZ","Syria":"SY","Kyrgyzstan":"KG","Kenya":"KE","S. Sudan":"SS","Suriname":"SR","Cambodia":"KH","El Salvador":"SV","Slovakia":"SK","Korea":"KR","Slovenia":"SI","Dem. Rep. Korea":"KP","Kuwait":"KW","Senegal":"SN","Sierra Leone":"SL","Kazakhstan":"KZ","Saudi Arabia":"SA","Sweden":"SE","Sudan":"SD","Dominican Rep.":"DO","Djibouti":"DJ","Denmark":"DK","Germany":"DE","Yemen":"YE","Algeria":"DZ","United States":"US","Uruguay":"UY","Lebanon":"LB","Lao PDR":"LA","Taiwan":"TW","Trinidad and Tobago":"TT","Turkey":"TR","Sri Lanka":"LK","Latvia":"LV","Lithuania":"LT","Luxembourg":"LU","Liberia":"LR","Lesotho":"LS","Thailand":"TH","Fr. S. Antarctic Lands":"TF","Togo":"TG","Chad":"TD","Libya":"LY","United Arab Emirates":"AE","Venezuela":"VE","Afghanistan":"AF","Iraq":"IQ","Iceland":"IS","Iran":"IR","Armenia":"AM","Albania":"AL","Angola":"AO","Argentina":"AR","Australia":"AU","Austria":"AT","India":"IN","Tanzania":"TZ","Azerbaijan":"AZ","Ireland":"IE","Indonesia":"ID","Ukraine":"UA","Qatar":"QA","Mozambique":"MZ"}


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
import random

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

def artistReturn(country= ""):
   id = music_graph.artist_country(country = country)["data"][0]["id"]
   print id
   raw = music_graph.get_tracks(id = id)["data"]
   raw = music_graph.get_spotify_id(id)
   print raw
"""
   while (booleanSpotifyId == False):
       n = random.randint(0,len(music_graph.get_tracks(id)["data"]))
       randTrack =  music_graph.get_tracks(id)["data"][n]
       print randTrack
       if "track_spotify_id"  in randTrack:
          spotify_id =  music_graph.get_tracks(id)["data"][n]["track_spotify_id"]
          booleanSpotifyId = True
   """



print artistReturn(country = "Israel")
   
