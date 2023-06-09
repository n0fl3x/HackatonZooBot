from commands.static_commands import HELP_COMMAND
from commands.quiz_commands import START_QUIZ_COMMAND


QUESTION_1 = """
Это текст первого вопроса.
"""


QUESTION_2 = """
Это текст второго вопроса.
"""


QUESTION_3 = """
Это текст третьего вопроса.
"""


QUESTION_4 = """
Это текст четвёртого вопроса.
"""


QUESTION_5 = """
Это текст пятого вопроса.
"""


END_MESSAGE = f"""
Тест окончен.\n
Если Вы хотите повторить тест, введите команду или нажмите /{START_QUIZ_COMMAND}
Чтобы вывести список всех доступных команд, введите или нажмите /{HELP_COMMAND}
"""


ALREADY_ANSWERED = f"""
Вы уже отвечали на этот вопрос
"""


ALREADY_FINISHED = f"""
Вы уже завершили этот опрос
"""
