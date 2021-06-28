#!/usr/bin/python3
# Главный файл всего этого дела но это и так понятно
# Немного импортов
from src import bot_module
from src import triggers_module
from src import rules_module
from src import anti_dvach_module
from src import capha_module
from src import settings
from typing import Union

# Инициализация необходимых параметров
CHAT_ID = bot_module.chat_id
CHAT_FILTER = bot_module.chat_filter
bot = bot_module.bot
dp = bot_module.dispather
types = bot_module.types

# Новый пользователь
@dp.message_handler(CHAT_FILTER, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_user(message: types.Message):
    # Вызов функции показа капчи
    await capha_module.send_capha(message)
    
# Размучивам нового пользователя и приветствуем его
@dp.callback_query_handler(CHAT_FILTER, text="unmute_new_user")
async def unmute_new_user(message: Union[types.CallbackQuery, types.Message]):
    # Вызов функции снятия мута с нового пользователя
    await capha_module.unmute_user(message)

# Бан бота ну или прсто невнимательного человека
@dp.callback_query_handler(CHAT_FILTER, text="ban_new_user")
async def ban_new_user(message: Union[types.CallbackQuery, types.Message]):
    # Вызов функции бана нового пользователя
    await capha_module.ban_user(message)

# Троллинг невнимательного юзера
@dp.callback_query_handler(CHAT_FILTER, text="fun_kik_new_user")
async def fun_kik_new_user(message: Union[types.CallbackQuery, types.Message]):
    # Вызов функции насмешек для нового пользователя
    await capha_module.kik_user(message)

# Показ правил
@dp.callback_query_handler(CHAT_FILTER, text="rules")
@dp.message_handler(CHAT_FILTER, commands=['rules'])
async def rules(message: Union[types.CallbackQuery, types.Message]):
    # Вызов функции показа правил в общем чате
    await rules_module.send_rules(message, types)

# Хэндлер триггеров
@dp.message_handler(lambda msg: any([y in msg.text.lower() for x in settings.triggers.keys() for y in x]))
async def reply_to_trigger(message: Union[types.CallbackQuery, types.Message]):
    # Вызов функции обработки и отправки триггера
    await triggers_module.send_trigger(message)

# Антидвач
@dp.message_handler(CHAT_FILTER, content_types=types.ContentTypes.ANY)
async def anti_dvach(message: Union[types.CallbackQuery, types.Message]):
    await anti_dvach_module.identification_of_message(message)

# Запускаем поллинг бота
if __name__ == "__main__":
    bot_module.executor.start_polling(dp, skip_updates=True)
