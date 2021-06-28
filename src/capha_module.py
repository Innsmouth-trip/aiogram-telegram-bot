# Модуль капчи
# Подключение необходимых модулей
from src import users_module
from src import supergroup_module
from src import bot_module
from src import welcome_module

# Загрузка необходимых параметров
bot = bot_module.bot
chat_id = bot_module.chat_id

# Создание капчи
async def send_capha(message):
    # Проверка на то новый ли это юзер
    if message.from_user not in message.new_chat_members:
        return

    # Сохранение данных о новом пользователе
    new_member = message.new_chat_members[0]
    users_module.add_new_user({
        'user_name' : new_member.first_name,
        'user_id' : new_member.id,
        'message_id' : message.message_id + 1
    })

    # Выдаем мут новому пользователю
    await supergroup_module.give_a_mute(new_member.id, "infinity")

    # Создаем капчу
    markup = bot_module.types.InlineKeyboardMarkup(row_width=2)
    item1 = bot_module.types.InlineKeyboardButton("Я бот", callback_data='ban_new_user')
    item2 = bot_module.types.InlineKeyboardButton("Я не бот", callback_data='unmute_new_user')
    item3 = bot_module.types.InlineKeyboardButton("Я не знаю кто я", callback_data='fun_kik_new_user')
    markup.add(item1, item2, item3)

    # Отправляем сообщение с капчей
    await message.reply("Вы бот?", reply_markup=markup)

# Снимаем бан с нового пользователя и приветствуем его
async def unmute_user(message):
    # Проверка пользователя
    if users_module.is_user_exist(message.from_user.id):
        # Получаем пользователя по id
        user = users_module.get_user_by_user_id(message.from_user.id)

        # Снятие мута с нового пользователя и удаление сообщения с капчей
        await supergroup_module.delete_message(user.get('message_id'))
        await supergroup_module.give_a_mute(user.get('user_id'), "unmute")

        # Отправка сообщения с приветствием
        await welcome_module.send_welcome_message(message)

        # Удаление пользователя из списка новых пользователей
        await users_module.remove_user_by_user_id(message.from_user.id)
    else:
        # Мут тролля
        await supergroup_module.give_a_mute(message.from_user.id, 70)

# Баним бота ну или просто невнимательного пользователя
async def ban_user(message):
    # Проверка на пользователя
    if users_module.is_user_exist(message.from_user.id):
        # Получаем пользователя по id
        user = users_module.get_user_by_user_id(message.from_user.id)

        # Бан пользователя и удаление сообщения с капчей
        await supergroup_module.delete_message(user.get('message_id'))
        await supergroup_module.give_a_ban(user.get('user_id'))

        # Отправка сообщения с извещением о том что пользователь бот
        await bot.send_message(chat_id, "Пошутил - проиграл")

        # Удаление пользователя из списка новых пользователей
        await users_module.remove_user_by_user_id(message.from_user.id)
    else:
        # Мут тролля
        await supergroup_module.give_a_mute(message.from_user.id, 70)

# Выкидываем пользователя из чата и насмехаемся над ним
async def kik_user(message):
    # Проверка на пользователя
    if users_module.is_user_exist(message.from_user.id):
        # Получаем пользователя по id
        user = users_module.get_user_by_user_id(message.from_user.id)

        # Удаляем сообщение с капчей и насмехаемся над пользователем
        await supergroup_module.delete_message(user.get('message_id'))
        await bot.send_message(chat_id, "Подумай над своим ответом")

        # Выкидываем пользователя из чата
        await supergroup_module.give_a_kik(user.get('user_id'))

        # Удаление пользователя из списка новых пользователей
        await users_module.remove_user_by_user_id(message.from_user.id)
    else:
        # Мут тролля
        await supergroup_module.give_a_mute(message.from_user.id, 70)
