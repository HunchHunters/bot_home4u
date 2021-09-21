import telebot;
from oauth2client.service_account import ServiceAccountCredentials
import gspread
bot = telebot.TeleBot('2007010693:AAFu7W_2QPBqllIUaJQE3AOtGjllv1wHyqE');


scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)

#creds = ServiceAccountCredentials.from_json('mypython-326612-6af17f4344e7.json')

client = gspread.authorize(creds)

python_test = client.open("Tilda_Form_4559105_20210916132823").sheet1


# @bot.message_handler(commands=['start'])
# def start(message):
#   user_id = message.from_user.id

@bot.message_handler(commands=['start'])

def send_welcome(message):

    user_name = message.from_user.username

    bot.reply_to(message, message.from_user.username)

bot.polling(none_stop=True, interval=0)
