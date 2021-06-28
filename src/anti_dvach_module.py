# Модуль для удаления сообщений с Двача
# Подлюкчени необходимых модулей
from src import bot_module
from src import supergroup_module
from src import settings

# Загрузка необходимых объектов
bot = bot_module.bot
chat_id = bot_module.chat_id

# Функция опознания сообщения
async def identification_of_message(message):
    if message.forward_from_chat.id in settings.id_black_list:
        await remove_message_and_mute_user(message)

# Удаление сообщения с двача и наказание юзера
async def remove_message_and_mute_user(message):
    # Удаление сообщения с двача
    await supergroup_module.delete_message(message.message_id)

    # Предупреждение пользователя
    await bot.send_message(chat_id, '<a href="tg://user?id={}">{}</a>, такое нельзя репостить'.format(message.from_user.id, message.from_user.first_name))
