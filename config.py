import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из файла .env

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
KINOPOISK_API_KEY = os.getenv("KINOPOISK_API_KEY")
DB_NAME = os.getenv("DB_NAME")

# os.getenv() позволяет получать значения переменных окружения

# dotenv:
# Позволяет хранить конфиденциальные данные (токены, ключи) в файле .env
