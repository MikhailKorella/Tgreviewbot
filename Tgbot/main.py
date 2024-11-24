from bot import bot
from handlers import start

# Обработчик команды /start
bot.message_handler(commands=['start'])(start)

# Запуск бота
bot.polling()
