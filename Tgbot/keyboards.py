import telebot
from telebot import types

# Клавиатура с выбором категории
def create_category_keyboard():
    """
    Возвращает клавиатуру с кнопками выбора категории
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Преподаватели'),
                 types.KeyboardButton('Образовательная программа'),
                 types.KeyboardButton('Студенческая жизнь'),
                 types.KeyboardButton('Кампус'),
                 types.KeyboardButton('Общежитие'),
                 types.KeyboardButton('Столовая'),
                 types.KeyboardButton('Здоровье и спорт'),
                 types.KeyboardButton('Трудоустройство и карьера'),
                 types.KeyboardButton('Технические вопросы'),
                 types.KeyboardButton('Другое'))
    return keyboard

# Клавиатура с выбором подкатегории в зависимости от категории
def create_subcategory_keyboard(category):
    """
    Принимает на вход category - категорию отзыва от прошлого выбора
    и возвращает клавиатуру с кнопками выбора подкатегории
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if category == 'Преподаватели':
        keyboard.add(types.KeyboardButton('Профессионализм'), 
                     types.KeyboardButton('Отношение к студентам'),
                     types.KeyboardButton('Организация занятий'),
                     types.KeyboardButton('Другое'))
    elif category == 'Образовательная программа':
        keyboard.add(types.KeyboardButton('Сложность материала'),
                     types.KeyboardButton('Качество материала'),
                     types.KeyboardButton('Доступность материала'),
                     types.KeyboardButton('Организация курса'),
                     types.KeyboardButton('Другое'))
    elif category == 'Студенческая жизнь':
        keyboard.add(types.KeyboardButton('Мероприятия'),
                     types.KeyboardButton('Клубы и организации'),
                     types.KeyboardButton('Коммуникация'),
                     types.KeyboardButton('Другое'))
    elif category == 'Кампус':
        keyboard.add(types.KeyboardButton('Инфраструктура'),
                     types.KeyboardButton('Чистота и порядок'),
                     types.KeyboardButton('Доступность'),
                     types.KeyboardButton('Другое'))
    elif category == 'Общежитие':
        keyboard.add(types.KeyboardButton('Инфраструктура'),
                     types.KeyboardButton('Чистота и порядок'),
                     types.KeyboardButton('Условия проживания'),
                     types.KeyboardButton('Доступность'),
                     types.KeyboardButton('Другое'))
    elif category == 'Столовая':
        keyboard.add(types.KeyboardButton('Качество еды'),
                     types.KeyboardButton('Цены'),
                     types.KeyboardButton('Обслуживание'),
                     types.KeyboardButton('Другое'))
    elif category == 'Здоровье и спорт':
        keyboard.add(types.KeyboardButton('Медицинские услуги'),
                     types.KeyboardButton('Спортивные клубы и секции'),
                     types.KeyboardButton('Здоровый образ жизни'),
                     types.KeyboardButton('Другое'))
    elif category == 'Трудоустройство и карьера':
        keyboard.add(types.KeyboardButton('Карьера после университета'),
                     types.KeyboardButton('Работа карьерного центра'),
                     types.KeyboardButton('Стажировки и практики'),
                     types.KeyboardButton('Другое'))
    elif category == 'Технические вопросы':
        keyboard.add(types.KeyboardButton('Сервисы'),
                     types.KeyboardButton('Wi-Fi и интернет'),
                     types.KeyboardButton('Оборудование'),
                     types.KeyboardButton('Другое'))
    else:
        keyboard.add(types.KeyboardButton('Другое'))
    return keyboard