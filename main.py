import telebot
import os
import sys
import requests


'''
if 'TOKEN' in os.environ:
    TOKEN = os.environ['TOKEN']
else:
    sys.exit("Telegram Bot Token not defined.")
'''
TOKEN='5707136883:AAEGJNVWfuI9dA5IWlfAk3pWgFvH-nheP3M'

JOBS_CHAT_ID='-1001134745498'
DEST_CHAT_ID='5707136883'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEXOhpi_l_iUP9jgDa7xYBFlHSQ3b18DgACoRAAAripWUrMPk3WN3WsGykE')
    bot.forward_message(message.chat.id, JOBS_CHAT_ID, 11260)


if __name__ == '__main__':
    bot.polling(none_stop=True)

