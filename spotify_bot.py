import spotipy
import telebot
from telebot import types
from spotipy.oauth2 import SpotifyOAuth
from spotipy import oauth2

bot = telebot.TeleBot('2012257190:AAE2r6U5BLjsksAjYJkGm0CNorwSH2oDHBw')

@bot.message_handler(commands=['start'])

def start(message):
    playlist_url = bot.send_message(message.chat.id, 'Поделись ссылкой на свой плейлист!')
    bot.register_next_step_handler(playlist_url, obtain_list_artists)


def obtain_list_artists(message):
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
    for song in pl_items:
        print(song["track"]["artists"][0]['name'])


bot.polling(none_stop=True, interval=0)
