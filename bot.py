import telebot
from telebot import types
import urllib
import dropbox
import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from parsing_gsheets import getListFromUsername,match
from parsing_dropbox import photo

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Tilda_Form_4559105_20210916132823").sheet1

bot = telebot.TeleBot('2012257190:AAE2r6U5BLjsksAjYJkGm0CNorwSH2oDHBw')

@bot.message_handler(commands=['start'])
def start(message):
    #user_char_data
    username = message.from_user.username
    user_data = getListFromUsername(username, sheet)
    name = user_data[0]
    #bot settings
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text='Начать', callback_data='start'+username)
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id, 'Привет, ' + name + '\n' + 'Посмотри, каких соседей мы тебе нашли!', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    username = call.data[5:]
    if call.message:
        if call.data[0:5] == 'start':
            #bot settings
            markup_inline = types.InlineKeyboardMarkup(row_width = 10)
            #data from username
            user_data = getListFromUsername(username, sheet)
            is_vaccined = user_data[6]
            name = user_data[0]
            url_photo = user_data[4]
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + name + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дальше', callback_data='dislike')
            markup_inline.add(dislike_butt,like_butt)

            text_to_reply = name+'\n'+is_vaccined
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id,text_to_reply, reply_markup=markup_inline)

        if call.data == 'dislike':
            #data from username
            user_data = match(username, sheet)
            is_vaccined = user_data[6]
            name = user_data[0]
            username = user_data[1]
            url_photo = user_data[4]
            price = user_data[8]
            #send emoji
            print(price[0:2])
            if int(price[0:2])<=20:
                money_emoji = '\U0001F4B2'*1
            elif int(price[0:2])<=30:
                money_emoji = '\U0001F4B2'*2
            else:
                money_emoji = '\U0001F4B2'*3
            text_to_reply = name+'\n'+'Бюджет ' +money_emoji
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.row_width = 7
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' +username + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дальше', callback_data='dislike')
            markup_inline.add(like_butt, dislike_butt)
            bot.send_photo(call.message.chat.id, photo(url_photo))
            bot.send_message(call.message.chat.id,text_to_reply+money_emoji, reply_markup=markup_inline)


bot.polling(none_stop=True, interval=0)
