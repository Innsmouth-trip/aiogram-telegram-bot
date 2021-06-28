# Модуль для работы с приветствием пользователя
# Подключение необходимых модулей
from src import bot_module
from src import supergroup_module
from src import settings

# Загрузка необходимых параметров
bot = bot_module.bot
chat_id = bot_module.chat_id
welcome_file = open("src/welcome_text.txt", "r+")
welcome_text = welcome_file.read()

# Функция вывода приветствия пользователя
async def send_welcome_message(message):
    # Создание кнопки с правилами
    markup = bot_module.types.InlineKeyboardMarkup(row_width=2)
    item1 = bot_module.types.InlineKeyboardButton("Правила", callback_data='rules')
    markup.add(item1)

    # Отправка стикера и текста приветствия в группу
    await supergroup_module.send_sticker("random")
    await bot.send_message(chat_id, welcome_text.format(message.from_user.id, message.from_user.first_name), reply_markup=markup)

# Функция изменения приветствия
async def change_welcome_text(message, new_welcome_text):
    # Проверка на админа
    if message.from_user.id in settings.admins:
        # Очистка файла от старого текста приветствия
        welcome_file.truncate()
        new_welcome_text = new_welcome_text.replace("/new_welcome_text ", "")

        # Запись нового текста приветствия и загрузка для использования
        welcome_file.write(new_welcome_text)
        welcome_text = rules.read()
    else:
        # Отправка сообщения с предупреждением
        await bot.send_message(chat_id, "Команда только для админов")