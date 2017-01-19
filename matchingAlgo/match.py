from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils
from utils import spotify
from utils import spotify_db_manager
import requests
import urllib, urllib2
import base64
import json
import time


print spotify.get_similar("marvin gaye","let's get it on")




