import telebot
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from telebot import types
import requests
import urllib
import dropbox
import re

dbx = dropbox.Dropbox('sl.A4_nfXji5QAYZd85KSOeIzJZbj_sLH8zQEHrXATWYl4kTOTj3xES40vZsUjcLRpnufzKimx1k9xosWaHQUe99fGMO-5ADYzfRGH_QozaNurp-JOvdHM4cMbQhtrFZn0pF9v0U2H__IoX')
bot = telebot.TeleBot('2007010693:AAFu7W_2QPBqllIUaJQE3AOtGjllv1wHyqE');
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
#creds = ServiceAccountCredentials.from_json('mypython-326612-6af17f4344e7.json')

client = gspread.authorize(creds)
sheet = client.open("Tilda_Form_4559105_20210916132823").sheet1

def parsing_gsheets(username):
    cell = sheet.find(username)
    row = cell.row
    return row


@bot.message_handler(commands=['start'])
def start(message):


    username = message.from_user.username
    row = parsing_gsheets(username)
    name = sheet.cell(row,1).value
    # markup=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup_inline = types.InlineKeyboardMarkup()
    start_butt = types.InlineKeyboardButton(text = 'Начать', callback_data = 'start')
    markup_inline.add(start_butt)
    bot.send_message(message.chat.id,'Привет, ' + name+'\n'+'Посмотри, каких соседей мы тебе нашли!',reply_markup=markup_inline)

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
    if call.message:
        if call.data == "start":
            
            row = 1
            markup_inline = types.InlineKeyboardMarkup()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
            username = call.message.from_user.username
            #Photo matched
            id_people = rows_list[1]
            link = sheet.cell(id_people,5).value
            req_bytes = requests.get(link).content
            my_json = req_bytes.decode()
            str = my_json
            exp = r'>\w{2,}.png'
            result = re.search(exp, str).group(0)
            file_name = result[1:]
            metadata, f = dbx.files_download('/Приложения/Tilda Publishing/'+file_name)
            bot.send_photo(call.message.chat.id, f.content)
            like_butt = types.InlineKeyboardButton(text='Лайк!', url='https://t.me/'+'followthesun'+'?start=+666')
            dislike_butt = types.InlineKeyboardButton(text = 'Дизлайк:(', callback_data = 'dislike')
            markup_inline.add(like_butt, dislike_butt)
            bot.send_message(call.message.chat.id,'Ваня, 22',reply_markup=markup_inline)

        if call.data =='dislike':
            bot.send_message(call.message.chat.id,'IW')




# @bot.message_handler(commands = ['switch'])
# def switch(message):
#     markup = types.InlineKeyboardMarkup()
#     switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="@followthesun")
#     markup.add(switch_button)
#     bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)


bot.polling(none_stop=True, interval=0)
