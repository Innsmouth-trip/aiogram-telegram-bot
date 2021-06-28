# Модуль для работы с правилами
# Модключение модуля бота и модуля параметров
from src import bot_module
from src import settings

# Закидывание необходимых параметров
bot = bot_module.bot
chat_id = bot_module.chat_id
rules = open("src/rules_text.txt", "r+")
rules_text = rules.read()

# Показ правил в общем чате
async def send_rules(message, types):
    # Отправка сообщения с правилами
    await bot.send_message(chat_id, rules_text)

    # Проверка был ли вызов через нажатие кнопки или через команду
    if isinstance(message, types.Message):
        return

    # Удаление кнопки
    await message.answer()
    await message.message.delete_reply_markup()

# Показ приватных правил
async def send_private_rules(user_id):
    # Отправка сообщения с правилами лично пользователю
    await bot.send_message(user_id, rules_text)

# Изменение правил чата
async def change_chat_rules(message, new_chat_rules_text):
    # Проверка на админа
    if message.from_user.id in settings.admins:
        rules.truncate()
        new_chat_rules_text = new_chat_rules_text.replace("/new_rules ", "")
        rules.write(new_chat_rules_text)
        rules_text = rules.read()
    else:
        await bot.send_message(chat_id, "Правила могут менять только админы")