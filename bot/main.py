import telebot
from telebot import types
import os
from dotenv import load_dotenv, find_dotenv
from parser_twt import Find_info
from collections import defaultdict


dotenv_path = load_dotenv(find_dotenv())

token = os.environ.get('TGTOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_messedge(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    login = types.KeyboardButton("Свиня")
    hash = types.KeyboardButton('Поиск по #')
    users = types.KeyboardButton('Найти посты юзера')
    keyboard.add(login, hash, users)
    bot.send_message(message.chat.id,'Привет, я подростающий бот, пришлите мне тег для поиска', reply_markup=keyboard)


@bot.message_handler(func=lambda msg: msg.text == "Свиня")
def reply_on_button(messege):
    filename = 'https://tenor.com/ru/view/pig-azamaz-gif-24202539'
    bot.send_animation(messege.chat.id, filename)

def get_tweet_by_hash(messege):
    if messege.text[0] == '#':
        bot.send_message(messege.chat.id, 'Неправильный набор')
        return False
    bot.send_message(messege.chat.id, 'начинаем поиск')

    finder = Find_info(messege.text)
    result = finder.find_by_hash()
    i = 0
    for item in result:
        bot.send_message(messege.chat.id, f'<b>Автор:</b> <code>{result["username"][i]}</code>\n <b>пост</b> <code>{result["content"][i]}</code>\n', parse_mode='HTML')
        try:
            bot.send_message(messege.chat.id, result['full'][i])
        except Exception as e:
            bot.send_message(messege.chat.id, 'no image in this post')
        i+=1


def get_user_tweets(messege):
    if messege.text[0] == '@':
        bot.send_message(messege.chat.id, 'Неправильный набор')
        return False
    

    finder = Find_info(messege.text)
    result = finder.find_user()
    i = 0
    for item in result:
        bot.send_message(messege.chat.id, f'<b>Автор:</b> <code>{result["username"][i]}</code>\n \n <b>Пост:\n</b> <code>{result["content"][i]}</code>\n', parse_mode='HTML')
        try:
            bot.send_message(messege.chat.id, result['full'][i])
        except Exception as e:
            bot.send_message(messege.chat.id, 'no image in this post')
        i+=1

@bot.message_handler(func=lambda msg: msg.text == 'Поиск по #' and msg.content_type == 'text')
def redirect_to_hash(messege):
    msg = bot.reply_to(messege, 'Введите тег')
    bot.register_next_step_handler(msg, get_tweet_by_hash)


@bot.message_handler(func=lambda msg: msg.text == 'Найти посты юзера' and msg.content_type == 'text')
def redirect_to_user(messege):
    msg = bot.reply_to(messege, 'Введите имя юзернейм')
    bot.register_next_step_handler(msg, get_user_tweets)

if __name__ == "__main__":
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()