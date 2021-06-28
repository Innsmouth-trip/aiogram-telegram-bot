# Модуль для работы с супер группами
# Подключение необходимых модулей
from src import bot_module
from src import settings
import time
import random

# Загрузка необходимых параметров
bot = bot_module.bot
chat_id = bot_module.chat_id
sticker_file = open("src/stickers.txt", "r+")

# Мут пользователя
async def give_a_mute(user_id, second):
    if second == "infinity":
        await bot.restrict_chat_member(chat_id, user_id)
    elif second == "unmute":
        await bot.restrict_chat_member(chat_id, user_id, permissions={"can_send_messages" : True, 
                                                                      "can_send_media_messages" : True, 
                                                                      "can_send_polls" : True, 
                                                                      "can_send_other_messages" : True, 
                                                                      "can_add_web_page_previews" : True,
                                                                      "can_invite_users" : True})
    else:
        await bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + int(second))

# Бан пользователя
async def give_a_ban(user_id):
    await bot.kick_chat_member(chat_id, user_id)

# Выкидываем пользователя из группы
async def give_a_kik(user_id):
    await bot.unban_chat_member(chat_id, user_id)

# --- Временный функционал ---

# Отправка стикера 
async def send_sticker(sticker):
    if sticker == "random":
        sticker = random.choice(settings.stikers)
        sticker = sticker.rstrip()
        await bot.send_sticker(chat_id, sticker, 'rb')
    else:
        await bot.send_sticker(chat_id, sticker, 'rb')

# --- Временный функционал ---

# Удаление сообщений
async def delete_message(message_id):
    await bot.delete_message(chat_id, message_id)
