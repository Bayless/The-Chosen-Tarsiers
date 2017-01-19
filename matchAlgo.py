# Designed, created, sweated, concieved by Jason

import utils
import random
#from utils import spotify
#from utils import spotify_db_manager
from utils import last_fm
import requests
import urllib, urllib2
import base64
import json
import time
availableCountries = {"Bangladesh":"BD","Belgium":"BE","Burkina Faso":"BF","Bulgaria":"BG","Bosnia and Herz.":"BA","Brunei":"BN","Bolivia":"BO","Japan":"JP","Burundi":"BI","Benin":"BJ","Bhutan":"BT","Jamaica":"JM","Botswana":"BW","Brazil":"BR","Bahamas":"BS","Belarus":"BY","Belize":"BZ","Russia":"RU","Rwanda":"RW","Serbia":"RS","Timor-Leste":"TL","Turkmenistan":"TM","Tajikistan":"TJ","Romania":"RO","Guinea-Bissau":"GW","Guatemala":"GT","Greece":"GR","Eq. Guinea":"GQ","Guyana":"GY","Georgia":"GE","United Kingdom":"GB","Gabon":"GA","Guinea":"GN","Gambia":"GM","Greenland":"GL","Ghana":"GH","Oman":"OM","Tunisia":"TN","Jordan":"JO","Croatia":"HR","Haiti":"HT","Hungary":"HU","Honduras":"HN","Puerto Rico":"PR","Palestine":"PS","Portugal":"PT","Paraguay":"PY","Panama":"PA","Papua New Guinea":"PG","Peru":"PE","Pakistan":"PK","Philippines":"PH","Poland":"PL","Zambia":"ZM","W. Sahara":"EH","Estonia":"EE","Egypt":"EG","South Africa":"ZA","Ecuador":"EC","Italy":"IT","Vietnam":"VN","Solomon Is.":"SB","Ethiopia":"ET","Somalia":"SO","Zimbabwe":"ZW","Spain":"ES","Eritrea":"ER","Montenegro":"ME","Moldova":"MD","Madagascar":"MG","Morocco":"MA","Uzbekistan":"UZ","Myanmar":"MM","Mali":"ML","Mongolia":"MN","Macedonia":"MK","Malawi":"MW","Mauritania":"MR","Uganda":"UG","Malaysia":"MY","Mexico":"MX","Israel":"IL","France":"FR","Somaliland":"XS","Finland":"FI","Fiji":"FJ","Falkland Is.":"FK","Nicaragua":"NI","Netherlands":"NL","Norway":"NO","Namibia":"NA","Vanuatu":"VU","New Caledonia":"NC","Niger":"NE","Nigeria":"NG","New Zealand":"NZ","Nepal":"NP","Kosovo":"XK","CU+00F4te d'Ivoire":"CI","Switzerland":"CH","Colombia":"CO","China":"CN","Cameroon":"CM","Chile":"CL","N. Cyprus":"XC","Canada":"CA","Congo":"CG","Central African Rep.":"CF","Dem. Rep. Congo":"CD","Czech Rep.":"CZ","Cyprus":"CY","Costa Rica":"CR","Cuba":"CU","Swaziland":"SZ","Syria":"SY","Kyrgyzstan":"KG","Kenya":"KE","S. Sudan":"SS","Suriname":"SR","Cambodia":"KH","El Salvador":"SV","Slovakia":"SK","Korea":"KR","Slovenia":"SI","Dem. Rep. Korea":"KP","Kuwait":"KW","Senegal":"SN","Sierra Leone":"SL","Kazakhstan":"KZ","Saudi Arabia":"SA","Sweden":"SE","Sudan":"SD","Dominican Rep.":"DO","Djibouti":"DJ","Denmark":"DK","Germany":"DE","Yemen":"YE","Algeria":"DZ","United States":"US","Uruguay":"UY","Lebanon":"LB","Lao PDR":"LA","Taiwan":"TW","Trinidad and Tobago":"TT","Turkey":"TR","Sri Lanka":"LK","Latvia":"LV","Lithuania":"LT","Luxembourg":"LU","Liberia":"LR","Lesotho":"LS","Thailand":"TH","Fr. S. Antarctic Lands":"TF","Togo":"TG","Chad":"TD","Libya":"LY","United Arab Emirates":"AE","Venezuela":"VE","Afghanistan":"AF","Iraq":"IQ","Iceland":"IS","Iran":"IR","Armenia":"AM","Albania":"AL","Angola":"AO","Argentina":"AR","Australia":"AU","Austria":"AT","India":"IN","Tanzania":"TZ","Azerbaijan":"AZ","Ireland":"IE","Indonesia":"ID","Ukraine":"UA","Qatar":"QA","Mozambique":"MZ"}




def match_spotify_seed(song = ""):
   trackID = spotify.search(search_field = song, type = "track")[0]
   audioFeatures = spotify.audio_features(songID)
   

   market =  availableCountries.get(random.choice(availableCountries.keys()))

   danceability = audioFeatures['danceability']
   acousticness = audioFeatures['acousticness']
   energy = audioFeatures['energy']
   instrumentalness = audioFeatures['instrumentalness']

   return spotify.get_recommendations(limit = 1, market = market,
                        max_danceability = 1.0, min_danceability = 0.0,
                        max_acousticness = 1.0, min acousticness = 0.0,
                        max_energy = 1.0, min_energy = 0.0,
                        max_instrumentalness = 1.0, min_instrumentalness = 0.0,
                        seed_tracks = ID)[0]









