import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

def normalize_str(string):
    return string.translate(str.maketrans('\\/:*?"<>|', "__       "))

def put_playlist_to_db(username, pl_uri):
    offset = 0
    fields = "items.track.artists.name"
    auth_manager_ = SpotifyClientCredentials(
            client_id ='68a67da9be1a4acaab7c640fba827795',
            client_secret = '5bd3941b4763402aac9fbc239b4b068a'
         )
    sp = spotipy.Spotify(auth_manager=auth_manager_)
    pl_name = sp.playlist(pl_uri)["name"]
    pl_items = sp.playlist_items(
        pl_uri,
        offset=offset,
        fields=fields,
        additional_types=["track"],
    )["items"]
    artist_str = ''
    for song in pl_items:
        print(song["track"]["artists"][0]['name'])
        artist_str = artist_str + '/next/' + str(song["track"]["artists"][0]['name'])

    import sqlite3
    connection = sqlite3.connect('db_spotify.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO SpotifyMatching ('username','Liked Artists') VALUES (?, ?)", (username,artist_str))
    connection.commit()

    return True
