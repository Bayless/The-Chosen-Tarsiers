from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils
from utils import spotify
import json

def match_last(artist="",track="",number = 5):
    raw =  spotify.get_similar(artist,track)
    for i in range(0,5):
        track =  raw['similartracks']["track"][i]['name']
        singer = raw['similartracks']["track"][i]['artist']["name"]
        print track + " : " + singer
