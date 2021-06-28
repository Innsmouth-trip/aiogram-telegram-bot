# Модуль тригеров
# Подключения необходимых модулей
from src import settings
from src import supergroup_module

# Обработчик тригеров
async def send_trigger(message):
    for trigger in settings.triggers.keys():
        for variation in trigger:
            if variation in message.text.lower().split():
                # Манжара
                if trigger == list(settings.triggers.keys())[4]:
                    await message.reply(settings.triggers[trigger].format(message.from_user.id, message.from_user.first_name))

                # Бан
                elif trigger == list(settings.triggers.keys())[1]:
                    await message.reply(settings.triggers[trigger])
                    await supergroup_module.give_a_mute(message.from_user.id, settings.fun_mute_time)

                # Все остальные
                else:
                    await message.reply(settings.triggers[trigger])
