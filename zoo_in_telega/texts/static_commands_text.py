import os

from commands.static_commands import (
    HELP_COMMAND,
    ABOUT_COMMAND,
    CONTACTS_COMMAND,
    CREATORS_COMMAND,
)

from commands.quiz_commands import START_QUIZ_COMMAND


START_COMMAND_TEXT = f"""
Вас приветствует "Зоопарк в телеге"!

Это развлекательный бот - проект Московского Зоопарка, созданный для поддержки программы опеки его обитателей.

Чтобы увидеть список всех команд и возможностей введите или нажмите /{HELP_COMMAND}

Также для навигации Вы можете использовать кнопку Меню возле поля ввода сообщения на Вашем устройстве.
"""


HELP_COMMAND_TEXT = f"""
Список доступных команд данного бота:


/{START_QUIZ_COMMAND} - запуск развлекательного опроса для определения Вашего тотемного животного

/{HELP_COMMAND} - вывести список доступных команд

/{ABOUT_COMMAND} - о нас

/{CONTACTS_COMMAND} - контакты Московского Зоопарка

/{CREATORS_COMMAND} - о создателях бота
"""


CONTACTS_COMMAND_TEXT = """
Актуальная информация о том, как с нами связаться:
"""


ABOUT_COMMAND_TEXT = """
Ссылки на наши ресурсы:
"""


CREATORS_COMMAND_TEXT = f"""
Данный бот создан командой разработчиков в составе:

Дарья Кузнецова - @camomail0_0
Роман Невзоров - @Nevzorov_r_o

при поддержке онлайн школы программирования SkillFactory.
2023 ©
"""
