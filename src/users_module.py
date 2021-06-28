# Модуль для работы с пользователями
# Инициализация списка
users = []

# Функция очистки списка
def reser_users():
    users.clear()

# Добавление нового пользователя
def add_new_user(user):
    users.append(user)

# Проверка существует ли пользователь в списке
def is_user_exist(user_id):
    return any(user['user_id'] == user_id for user in users)

# Удаление пользователя по id
def remove_user_by_user_id(user_id):
    users[:] = [user for user in users if user.get('user_id') != user_id]

# Получение пользователя по id
def get_user_by_user_id(user_id):
    if is_user_exist(user_id):
        return next(user for user in users if user['user_id'] == user_id)
    else:
        return False