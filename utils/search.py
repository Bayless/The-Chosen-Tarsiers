import music_graph

def search(query = '', offset = 1):
    response = music_graph.get_similar_song_name(query, offset)

    to_return = []

    for song in response['data']:
        if 'track_spotify_id' in song:
            new_song_dict = {}
            new_song_dict['spotifyId'] = song['track_spotify_id']
            new_song_dict['title'] = song['title']
            new_song_dict['artistName'] = song['artist_name']            
            to_return.append(new_song_dict)

    return to_return

print search('Hello Goodbye')
