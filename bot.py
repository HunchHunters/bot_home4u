import telebot;
bot = telebot.TeleBot('2007010693:AAFu7W_2QPBqllIUaJQE3AOtGjllv1wHyqE');


# @bot.message_handler(commands=['start'])
# def start(message):
#   user_id = message.from_user.id

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, message.from_user.id)

bot.polling(none_stop=True, interval=0)
