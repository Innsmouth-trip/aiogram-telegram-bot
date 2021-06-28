# Модуль содержащий бота
# Немного импортов
import os
from typing import Union
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.builtin import IDFilter

# Загрузка всяких параметров
load_dotenv(os.path.join('.', '.env'))
chat_id = os.getenv("CHAT_ID")
token = str(os.getenv("TOKEN"))
chat_filter = IDFilter(chat_id=chat_id)

# Инициализация бота
bot = Bot(token=token, parse_mode="HTML")
dispather = Dispatcher(bot)