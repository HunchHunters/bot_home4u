import telebot
from telebot import types
import urllib
import dropbox
import re
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from parsing_memes import meme_matching,find_name,find_link_photo
from parsing_dropbox import photo

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Tilda_Form_4559105_20210922195121").sheet1
bot = telebot.TeleBot('2037831985:AAGKohGKMRlAH-LuciaVefOzNPoN0kyfWIw')

@bot.message_handler(commands=['start'])
def start(message):
    username = message.chat.username
    print(username)
    name = find_name(sheet,username)
    #user_char_data
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text='Начать', callback_data ='start'+username)
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id, 'Привет, '+ name , reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    username = call.data[5:]
    users_list = meme_matching(sheet, username)
    users_gen = gereratorUsers(users_list)
    print(next(users_gen))
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


# def gereratorUsers(argument):
#     try:
#         yield argument
#     except StopIteration:
#         return argument[0]


bot.polling(none_stop=True, interval=0)
