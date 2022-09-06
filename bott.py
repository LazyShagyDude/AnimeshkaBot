import random
import requests
import re
import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN',parse_mode='html')


def get_url():
    contents = requests.get('https://waifu.pics/api/sfw/waifu').json()
    url = contents['url']
    return url


def get_nsfw():
    contents = requests.get('https://waifu.pics/api/nsfw/waifu').json()
    url = contents['url']
    return url


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вайфу")
    item2 = types.KeyboardButton("Хорни")
    item3 = types.KeyboardButton("Аниме")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    mess = f'Привет,<b>{message.from_user.first_name} , я просто Анимешный Бот </b>'
    bot.send_message(message.chat.id, mess,
                     reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Вайфу":
        url = get_url()
        photo = url
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Хорни":
        url = get_nsfw()
        photo = url
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Аниме":
        contents = requests.get('https://api.jikan.moe/v4/random/anime', timeout=5).json()
        data=contents.get("data")
        image=data.get('images').get('jpg').get("large_image_url")
        name=data.get('title')
        url=data.get('url')
        year = data.get('season')
        episod = data.get('episodes')
        mes1 = f'<a href="{url}">{name}</a>'
        mes2 = f'<b>Эпизодов: {episod}</b>'
        mes3 = f'Сезон: {year}'
        print(year)
        bot.send_photo(message.chat.id, image,
                           caption=mes1)
        bot.send_message(message.chat.id, mes2)
        bot.send_message(message.chat.id, mes3)




bot.polling(none_stop=True)