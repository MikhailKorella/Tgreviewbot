import telebot
from config import TOKEN
from handlers import start

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
bot.message_handler(commands=['start'])(start)

# Запуск бота
bot.polling()