import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2
from urllib.parse import quote

def normalize_str(string):
    return string.translate(str.maketrans('\\/:*?"<>|', "__       "))

def get_playlist_by_url(pl_uri):
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
        artist_str = artist_str = str(song["track"]["artists"][0]['name'])

        artist_list = []
        artist_list.append()
get_playlist_by_url('https://open.spotify.com/playlist/1grOq7gkGG1Z0JHOVX1Olj')
