import telebot
from telebot import types
import urllib
import dropbox
import re
import gspread
import random
import spotipy
import telebot
from telebot import types
from spotipy.oauth2 import SpotifyOAuth
from spotipy import oauth2

from oauth2client.service_account import ServiceAccountCredentials
from parsing_memes import meme_matching, find_name, find_link_photo
from parsing_db import ListIterator, parsing
from parsing_dropbox import photo
from spotify import put_playlist_to_db

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Tilda_Form_4559105_20210922195121").sheet1
bot = telebot.TeleBot('2037831985:AAGKohGKMRlAH-LuciaVefOzNPoN0kyfWIw')

@bot.message_handler(commands=['start'])
def start(message):
    username = message.chat.username
    name = find_name(sheet,username)
    #user_char_data
    markup_inline = types.InlineKeyboardMarkup()
    yes_butt = types.InlineKeyboardButton(text='Да!', callback_data ='has spotify')
    no_butt = types.InlineKeyboardButton(text='Нет:(', callback_data ='no spotify')
    markup_inline.add(yes_butt, no_butt)
    playlist_url = bot.send_message(message.chat.id, 'У тебя есть spotify?')


@bot.message_handler(content_types=["text"])
def process_playlist(message):
    username = message.chat.username
    playlist_url = message.text
    put_playlist_to_db(username, playlist_url)

@bot.callback_query_handler(func=lambda call: True)

def start_callback(call):
    if call.data == 'has spotify':
        playlist_url = bot.send_message(message.chat.id, 'Поделись ссылкой на свой плейлист в spotify!')



def callback_inline(call):
    # Если сообщение из чата с ботом
    username = call.data[5:]
    meme_users = meme_matching(sheet, username)
    music_match = parsing(username)
    match_meme = ListIterator(meme_users)
    match_music = ListIterator(music_match)

    if call.message:
        if call.data[0:5] == 'start':
            #bot settings
            try:
                user_name = next(users_gen)
            except StopIteration:
                bot.send_message(call.message.chat.id,'Пользователи закончились:(', reply_markup=markup_inline)

            markup_inline = types.InlineKeyboardMarkup(row_width = 7)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data='dlike'+username)
            markup_inline.add(dislike_butt,like_butt)
            # text_to_reply = name+'\n'+is_vaccined
            url_photo = find_link_photo(sheet,user_name)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id,'msg', reply_markup=markup_inline)

        if call.data[0:5] == 'dlike':
            username = call.data[5:]
            user_name = next(users_gen)
            markup_inline = types.InlineKeyboardMarkup(row_width = 7)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data='dlike'+username)
            markup_inline.add(dislike_butt,like_butt)
            # text_to_reply = name+'\n'+is_vaccined
            url_photo = find_link_photo(sheet, user_name)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id,'msg', reply_markup=markup_inline)



bot.polling(none_stop=True, interval=0)
