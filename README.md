# The Chosen Tarsiers
## Soft Dev Fall Final Project: Magic Music Matcher
### Magic Matchers:
- Bayle Smith-Salzberg (Prime Minister)
- Rodda R. John (Interior Minister)
- Anya Keller (Communications Minister)
- Jason Mohabir (Foreign Minister)

The Magic Music Matcher allows you to diversify your playlist. You may click on any country and will be given a popular song from that country. You can then click on the compare button and you will be given 5 more similar songs from a different country. Our unique algorithm for comparing the songs takes into consideration aspects of songs to suggest musically similar, but geographically different songs for you to listen to. On top of having access to songs from different countries, you can search for your personal favorite tunes and look for similar songs using the same matching algorithms. Music is a major key to success, and The Music Thing will find you all the keys. 

watch our demo here: [Demo of Awesome](https://youtu.be/QIIgQ24DRZw)

Do some things to run this properly:

secure your own keys and store them in files called: music_graph_key (for the music graph API key which enables us to find the country of origin of the artist) and spotify_key (for the spotify API key where we find the musical attributes and through which we play the songs) in the utils folder.

Run:

`$ pip install Flask`

`$ pip install requests`

`$ python utils/initialize.py`

`$ python app.py`

Make some magic!
