from datetime import datetime
from keyboards import create_category_keyboard, create_subcategory_keyboard
from main import bot
from config import sheet

# Обработчик старта
def start(message):
    """
    Отправляет пользователю приветственное сообщение и 
    предлагает выбрать категорию отзыва. 
    На вход принимает аргумент message - сообщение пользователя
    """
    bot.send_message(
        message.chat.id,
        "Здравствуйте, мы собираем отзывы о жизни в университете, чтобы сделать ее еще лучше! Пожалуйста, выберите категорию, по которой вы хотите оставить отзыв:",
        reply_markup=create_category_keyboard()
    )

# Обработчик выбора категории
@bot.message_handler(func=lambda message: message.text in [
    "Преподаватели", "Образовательная программа", "Студенческая жизнь", "Кампус", "Общежитие",
    "Столовая", "Здоровье и спорт", "Трудоустройство и карьера", "Технические вопросы", "Другое"
])
def category_chosen(message):
    """ 
    Принимает на вход message - сообщение пользователя
    Отправляет клавиатуру с выбором подкатегории
    """
    category = message.text
    bot.send_message(
        message.chat.id,
        f"Отлично! Вы выбрали категорию {category}. Теперь выберите подкатегорию:",
        reply_markup=create_subcategory_keyboard(category)
    )
    bot.register_next_step_handler(message, subcategory_chosen, category)

# Обработчик выбора курса
def subcategory_chosen(message, category):
    """
    Принимает на вход message - сообщение пользователя и category - категорию отзыва
    Запрашивает сообщение от пользователя
    """
    subcategory = message.text
    user = message.from_user.username if message.from_user.username else f"{message.from_user.first_name} {message.from_user.last_name}"
    current_date = datetime.now().strftime("%Y-%m-%d")
    bot.send_message(message.chat.id, "Отлично! Теперь, пожалуйста, введите свое сообщение:")
    bot.register_next_step_handler(message, process_message, category, subcategory, user, current_date)

# Обработчик ввода сообщения и сохранение в таблицу
def process_message(message, category, subcategory, user, current_date):
    """
    Принимает на вход message - сообщение пользователя, category - выбранную категорию отзыва,
    subcategory - выбранную подкатегорию, user - имя пользователя, current_date - текущую дату
    Обрабатывает введённое сообщение и сохраняет данные в гугл таблицу
    """
    data = [category, subcategory, user, current_date, message.text]
    sheet.append_row(data)
    bot.send_message(message.chat.id, "Данные успешно сохранены. Спасибо за ваш отзыв!")