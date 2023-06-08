from commands.static_commands import (
    HELP_COMMAND,
    ABOUT_COMMAND,
    CONTACTS_COMMAND,
    CREATORS_COMMAND,
)

from commands.question_buttons_commands_text import START_QUIZ_COMMAND


START_COMMAND_TEXT = f"""Привет!\n
Это развлекательный бот, созданный для поддержки программы опеки животных Московского Зоопарка.
Чтобы увидеть список всех команд и возможностей введите или нажмите /{HELP_COMMAND}"""


HELP_COMMAND_TEXT = f"""Список доступных команд данного бота:\n
/{START_QUIZ_COMMAND} - запуск развлекательного опроса для определения Вашего тотемного животного
/{HELP_COMMAND} - вывести список доступных команд 
/{ABOUT_COMMAND} - о нас
/{CONTACTS_COMMAND} - контакты Московского Зоопарка
/{CREATORS_COMMAND} - о создателях бота"""


CONTACTS_COMMAND_TEXT = """Актуальная информация о том, как с нами связаться:"""


ABOUT_COMMAND_TEXT = """Ссылки на наши ресурсы:"""


CREATORS_COMMAND_TEXT = """Данный бот создан командой разработчиков Team_6 в составе:
<имена и фамилии>

при поддержке онлайн школы программирования SkillFactory.
2023"""


NOT_NONE_STATE_CANCEL_COMMAND_TEXT = f"""Вы остановили опрос.
Если вы захотите вновь пройти его, то придётся начать сначала.
Для этого введите команду или нажмите /{START_QUIZ_COMMAND}\n
Для вывода всех доступных команд - /{HELP_COMMAND}"""


NONE_STATE_CANCEL_COMMAND_TEXT = """Вы ещё не приступили к новому опросу."""
