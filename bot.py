import telebot
import random
import os
from telebot import types

# Берем токен из секретов GitHub
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

options = ["Камень", "Ножницы", "Бумага"]

def get_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [types.KeyboardButton(opt) for opt in options]
    markup.add(*btns)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Привет! Давай сыграем в Камень, Ножницы, Бумага. Выбирай свой вариант:", 
        reply_markup=get_keyboard()
    )

@bot.message_handler(func=lambda message: message.text in options)
def play(message):
    user_choice = message.text
    bot_choice = random.choice(options)
    
    if user_choice == bot_choice:
        result = "🤝 Ничья!"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "🎉 Ты победил!"
    else:
        result = "💻 Я победил!"

    msg = f"Твой выбор: {user_choice}\nМой выбор: {bot_choice}\n\n{result}"
    bot.send_message(message.chat.id, msg, reply_markup=get_keyboard())

# Это самая важная строчка, чтобы бот не выключался!
bot.infinity_polling()
