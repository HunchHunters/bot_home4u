import telebot
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types
import requests
import urllib
import dropbox
import re
from parsing_gsheets import getListFromUsername

dbx = dropbox.Dropbox('sl.A4_nfXji5QAYZd85KSOeIzJZbj_sLH8zQEHrXATWYl4kTOTj3xES40vZsUjcLRpnufzKimx1k9xosWaHQUe99fGMO-5ADYzfRGH_QozaNurp-JOvdHM4cMbQhtrFZn0pF9v0U2H__IoX')
bot = telebot.TeleBot('2007010693:AAFu7W_2QPBqllIUaJQE3AOtGjllv1wHyqE')



def matching(user_str, match_str):
    cell = sheet.find(username)
    #user_str - string data from user

@bot.message_handler(commands=['start'])
def start(message):

    username = message.from_user.username
    row = getRowNum(username)
    name = sheet.cell(row,1).value
    # markup=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text='Начать', callback_data='start'+username)
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id, 'Привет, ' + name + '\n' + 'Посмотри, каких соседей мы тебе нашли!', reply_markup=markup_inline)

    #check_photo_name
    # link = sheet.cell(row,5).value
    # req_bytes = requests.get(link).content
    # my_json = req_bytes.decode()
    # str = my_json
    #
    # exp = r'>\w{2,}.png'
    # result = re.search(exp, str).group(0)
    # #print(result.group(0))
    # # start_index = my_json.find('?dl=0">')
    # # finish_index = my_json.find('</a>')
    # file_name = result[1:]
    # print(file_name)
    # metadata, f = dbx.files_download('/Приложения/Tilda Publishing/'+file_name)
    # bot.send_photo(message.chat.id, f.content)
    # bot.reply_to(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    username = call.data[5:]
    if call.message:
        if call.data[0:5] == 'start':
            row = 1

            #bot settings
            markup_inline = types.InlineKeyboardMarkup()
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/' + username + '?start=+666')
            dislike_butt = types.InlineKeyboardButton(text='Дизлайк:(', callback_data='dislike')
            markup_inline.add(like_butt, dislike_butt)

            #data from username
            usernameList = getListFromUsername(username)
            link = usernameList[4]
            is_vaccined = usernameList[6]
            name = usernameList[1]

            text_to_result = name+'\n'+is_vaccined
            #Photo matched
            req_bytes = requests.get(link).content
            my_json = req_bytes.decode()
            str = my_json
            exp = r'>\w{2,}.png'
            result = re.search(exp, str).group(0)
            file_name = result[1:]
            # metadata, f = dbx.files_download('/Приложения/Tilda Publishing/' + file_name)
            # bot.send_photo(call.message.chat.id, f.content)


            #text_to_reply =

            bot.send_message(call.message.chat.id,'asdf', reply_markup=markup_inline)

        if call.data == 'dislike':
            bot.send_message(call.message.chat.id, 'IW')

# @bot.message_handler(commands = ['switch'])
# def switch(message):
#     markup = types.InlineKeyboardMarkup()
#     switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="@followthesun")
#     markup.add(switch_button)
#     bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)

bot.polling(none_stop=True, interval=0)
