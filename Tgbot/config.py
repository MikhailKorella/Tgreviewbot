"""
Модуль для конфигурации бота, включая токен и подключение к Google Sheets.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Здесь можно ввести токен вашего бота и данные таблицы, в которую вы хотите собирать отзывы 
TOKEN = "токен"
JsonFile = "json файл"
GoogleTable = "название таблицы"

# Настройки Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # Cписок URL-адресов, которые указывают на доступы, необходимые приложению
creds = ServiceAccountCredentials.from_json_keyfile_name(JsonFile, scope) # Создается объект ServiceAccountCredentials из JSON-файла, содержащего учетные данные сервисного аккаунта
client = gspread.authorize(creds) # Авторизация для доступа к Google Sheets
sheet = client.open(GoogleTable).sheet1 # Открытие таблицы на первом листе
