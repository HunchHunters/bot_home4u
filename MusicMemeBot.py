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
from parsing_memes import meme_matching, find_name, find_link_photo,find_name
from parsing_db import ListIterator, parsing, obtain_songs
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
    yes_butt = types.InlineKeyboardButton(text = 'Музыка', callback_data = 'yemus' + username)
    no_butt = types.InlineKeyboardButton(text = 'Мемчики', callback_data =' stmem' + username)
    markup_inline.add(yes_butt, no_butt)
    bot.send_message(message.chat.id, 'Хотите мэтчи по музыке или по мемам?', reply_markup = markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def start_callback(call):
    try:
        username = call.data[5:]
        music_match = parsing(username)
        match_music = ListIterator(music_match)
    except StopIteration:
        markup_inline = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id,'Больше нет пользователей:(',reply_markup=markup_inline)

    if call.data[0:5] == 'yemus':
        playlist_url = bot.send_message(call.message.chat.id, 'Поделись ссылкой на свой плейлист в spotify!')
        bot.register_next_step_handler(playlist_url, matching_for_music)

    if call.data[0:5] == 'stmus':
        try:
            user_name = next(match_music)
            markup_inline_ = types.InlineKeyboardMarkup()
            music_match = parsing(user_name)
            random_songs = obtain_songs(user_name)
            song_str = ''
            for song in random_songs:
                song_str = song_str +song + '\n'
                print(song_str)
            url_photo = find_link_photo(sheet, user_name)
            like_butt_ = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt_ = types.InlineKeyboardButton(text='Дизлайк:(', callback_data ='dl')
            markup_inline_.add(dislike_butt_,like_butt_)
            bot.send_photo(call.message.chat.id, photo(url_photo))

            bot.send_message(call.message.chat.id, song_str, reply_markup = markup_inline_)

        except StopIteration and TypeError:
            markup_inline = types.InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id,'Больше нет пользователей:(',reply_markup=markup_inline)


    if call.data[0:5] == 'dlmus':
        try:
            user_name = next(match_music)
            markup_inline = types.InlineKeyboardMarkup()
            music_match = parsing(user_name)
            random_songs = obtain_songs(user_name)
            song_str = ''
            for song in random_songs:
                song_str = song_str +'\n'
            url_photo = find_link_photo(sheet, user_name)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data ='dl')
            markup_inline.add(dislike_butt,like_butt)
            #bot.send_photo(call.message.chat.id, photo(url_photo))
            #bot.send_message(call.message.chat.id, song_str, reply_markup = markup_inline)

        except StopIteration and TypeError:
            bot.send_message(call.message.chat.id, 'Больне нет пользователей:()', reply_markup = markup_inline)


    if call.data[0:5] == 'stmem':
        match_memes = ListIterator(music_match)
        try:
            markup_inline = types.InlineKeyboardMarkup()
            user_name = next(match_memes)
            url_photo = find_link_photo(sheet, user_name)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data ='dl')
            markup_inline.add(dislike_butt,like_butt)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            name = find_name(sheet, username)
            bot.send_message(call.message.chat.id, name, reply_markup=markup_inline)
        except StopIteration and TypeError:
            markup_inline = types.InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id,'Больше нет пользователей',reply_markup=markup_inline)

    if call.data[0:5] == 'dlmem':
        try:
            user_name = next(match_music)
            markup_inline = types.InlineKeyboardMarkup()
            music_match = parsing(user_name)
            random_songs = obtain_songs(user_name)
            song_str = ''
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data ='dl')
            markup_inline.add(dislike_butt,like_butt)
            bot.send_message(call.message.chat.id, song_str, reply_markup = markup_inline)
            bot.send_photo(call.message.chat.id, photo(url_photo))

        except StopIteration and TypeError:
            print('end')

# def callback_inline(match_music, call):
#     user_name = next(match_music)
#     markup_inline = types.InlineKeyboardMarkup()
#     url_photo = find_link_photo(sheet,user_name)
#     like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
#     dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data ='dlike'+username)
#     markup_inline.add(dislike_butt,like_butt)
#     bot.send_photo(call.message.chat.id, photo(url_photo))
#     bot.send_message(call.message.chat.id,'msg', reply_markup = markup_inline)


# if call.message:
#         # if call.data[0:5] == 'start':
        #     #bot settings
        #     try:
        #         user_name = next(users_gen)
        #     except StopIteration:
        #         bot.send_message(call.message.chat.id,'Пользователи закончились:(', reply_markup=markup_inline)
        #
        #     markup_inline = types.InlineKeyboardMarkup(row_width = 7)
        #     like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
        #     dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data='dlike'+username)
        #     markup_inline.add(dislike_butt,like_butt)
        #     # text_to_reply = name+'\n'+is_vaccined
        #     url_photo = find_link_photo(sheet,user_name)
        #     bot.send_photo(call.message.chat.id, photo(url_photo))
        #     bot.send_message(call.message.chat.id,'msg', reply_markup=markup_inline)

    if call.data[0:5] == 'dlike':
        try:
            user_name = next(users_gen)
            print(users_name)
        except StopIteration:
            ptint('end')

@bot.message_handler(content_types=['text'])
def matching_for_music(message):
    username = message.chat.username
    playlist_url = message.text
    put_playlist_to_db(username, playlist_url)
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text='начать!', callback_data ='stmus'+username )
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id, 'Хороший вкус!', reply_markup = markup_inline)

bot.polling(none_stop=True, interval=0)
