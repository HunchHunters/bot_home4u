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
    I_mem, I_mus = 0, 0
    username = message.chat.username
    name = find_name(sheet,username)
    #user_char_data
    markup_inline = types.InlineKeyboardMarkup()
    yes_butt = types.InlineKeyboardButton(text = 'Музыка', callback_data = str(I_mus)  + '|' + 'yemus' + username)
    no_butt = types.InlineKeyboardButton(text = 'Мемчики', callback_data = str(I_mem)  + '|' +'stmem' + username)
    markup_inline.add(yes_butt, no_butt)
    bot.send_message(message.chat.id, 'Хотите мэтчи по музыке или по мемам?', reply_markup = markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def start_callback(call):

    second_param = call.data.split('|')[1]
    username = second_param[5:]
    print(call.data)
    print(username)
    meme_match = meme_matching(sheet, username)
    print(meme_match)
    try:
        music_match = parsing(username)
    except StopIteration:
        pass
###########START MUSIC MENU##########################
    if second_param[0:5] == 'yemus':
        playlist_url = bot.send_message(call.message.chat.id, 'Поделись ссылкой на свой плейлист в spotify!')
        bot.register_next_step_handler(playlist_url, matching_for_music)
###########START MUSIC MATCH##########################
    if second_param[0:5] == 'stmus':
        I_mus = int( call.data.split('|')[0])
        if I_mus < len(music_match):
            user_name = music_match[I_mus]
            I_mus = I_mus + 1
            markup_inline_ = types.InlineKeyboardMarkup()
            music_match = parsing(user_name)
            random_songs = obtain_songs(user_name)
            song_str = ''
            for song in random_songs:
                song_str = song_str +song + '\n'
                #print(song_str)
            url_photo = find_link_photo(sheet, user_name)
            like_butt_ = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt_ = types.InlineKeyboardButton(text='Дизлайк:(', callback_data = str(I_mus)  + '|'+'dlmus'+username)
            markup_inline_.add(dislike_butt_,like_butt_)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id, song_str, reply_markup = markup_inline_)
        else:
            I_mus = 0
            dislike_butt_ = types.InlineKeyboardButton(text='Начнем сначала?', callback_data = str(I_mus)  + '|'+'dlmus'+username)
            markup_inline_.add(dislike_butt_)
            markup_inline_ = types.InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id, 'Пользователи закончились', reply_markup = markup_inline_)

    if second_param[0:5] == 'dlmus':
        I_mus = int( call.data.split('|')[0])
        if I_mus < len(music_match):
            print(music_match)
            user_name = music_match[I_mus]
            I_mus = I_mus + 1
            markup_inline_ = types.InlineKeyboardMarkup()
            music_match = parsing(user_name)
            random_songs = obtain_songs(user_name)
            song_str = ''
            for song in random_songs:
                song_str = song_str +song + '\n'
                #print(song_str)
            url_photo = find_link_photo(sheet, user_name)
            like_butt_ = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt_ = types.InlineKeyboardButton(text='Дизлайк:(', callback_data =str(I_mus)+ '|' +'dlmus' + username)
            markup_inline_.add(dislike_butt_,like_butt_)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id, song_str, reply_markup = markup_inline_)
        else:
            I_mus = 0
            markup_inline_ = types.InlineKeyboardMarkup()
            dislike_butt_ = types.InlineKeyboardButton(text='Начнем сначала?', callback_data = str(I_mus)  + '|'+'dlmus'+username)
            markup_inline_.add(dislike_butt_)
            bot.send_message(call.message.chat.id, 'Пользователи закончились', reply_markup = markup_inline_)


    if second_param[0:5] == 'stmem':

        username = second_param[5:]
        I_mem = int(call.data.split('|')[0])
        if I_mem < len(meme_match):
            user_name = meme_match[I_mem]
            markup_inline = types.InlineKeyboardMarkup()
            url_photo = find_link_photo(sheet, user_name)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data = str(I_mem)  + '|'+'dlmem'+username)
            markup_inline.add(dislike_butt,like_butt)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            name = find_name(sheet, username)
            bot.send_message(call.message.chat.id, name, reply_markup=markup_inline)
        else:
            I_mem = 0
            dislike_butt_ = types.InlineKeyboardButton(text='Начнем сначала?', callback_data = str(I_mem)  + '|'+'dlmem'+username)
            markup_inline_.add(dislike_butt_)
            markup_inline_ = types.InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id, 'Пользователи закончились', reply_markup = markup_inline_)

    if second_param[0:5] == 'dlmem':
        I_mem = int( call.data.split('|')[0])
        if I_mem < len(meme_match):
            user_name = meme_match[I_mem]
            I_mem = I_mem + 1
            markup_inline = types.InlineKeyboardMarkup()
            url_photo = find_link_photo(sheet, user_name)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + user_name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data = str(I_mem)  + '|'+'dlmem'+username)
            name = find_name(sheet, username)
            markup_inline.add(dislike_butt,like_butt)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id, name, reply_markup = markup_inline)
        else:
            I_mem = 0
            dislike_butt_ = types.InlineKeyboardButton(text='Начнем сначала?', callback_data = str(I_mem)  + '|'+'dlmem'+username)
            markup_inline_ = types.InlineKeyboardMarkup()
            markup_inline_.add(dislike_butt_)
            markup_inline_ = types.InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id, 'Пользователи закончились', reply_markup = markup_inline_)

@bot.message_handler(content_types=['text'])
def matching_for_music(message):
    I_mus = 0
    username = message.chat.username
    playlist_url = message.text
    put_playlist_to_db(username, playlist_url)
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text='начать!', callback_data =str(I_mus)  + '|''stmus'+username )
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id, 'Хороший вкус!', reply_markup = markup_inline)

bot.polling(none_stop=True, interval=0)
