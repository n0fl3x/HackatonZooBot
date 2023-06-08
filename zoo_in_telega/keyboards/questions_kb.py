from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from commands.question_buttons_commands_text import CANCEL_COMMAND


# CANCEL
inline_btn_cancel = InlineKeyboardButton(
    text='Остановить опрос',
    callback_data=f'/{CANCEL_COMMAND}',
)


# QUESTION 1
inline_btn_1_1 = InlineKeyboardButton(
    text='1',
    callback_data='1 inl btn',
)

inline_btn_1_2 = InlineKeyboardButton(
    text='2',
    callback_data='2 inl btn',
)

inline_btn_1_3 = InlineKeyboardButton(
    text='3',
    callback_data='3 inl btn',
)

inline_btn_1_4 = InlineKeyboardButton(
    text='4',
    callback_data='4 inl btn',
)

inline_keyboard_1 = InlineKeyboardMarkup().\
    row(inline_btn_1_1).\
    row(inline_btn_1_2).\
    row(inline_btn_1_3).\
    row(inline_btn_1_4).\
    row(inline_btn_cancel)


# QUESTION 2
inline_btn_2_1 = InlineKeyboardButton(
    text='5',
    callback_data='5 inl btn',
)

inline_btn_2_2 = InlineKeyboardButton(
    text='6',
    callback_data='6 inl btn',
)

inline_btn_2_3 = InlineKeyboardButton(
    text='7',
    callback_data='7 inl btn',
)

inline_btn_2_4 = InlineKeyboardButton(
    text='8',
    callback_data='8 inl btn',
)

inline_keyboard_2 = InlineKeyboardMarkup().\
    row(inline_btn_2_1).\
    row(inline_btn_2_2).\
    row(inline_btn_2_3).\
    row(inline_btn_2_4).\
    row(inline_btn_cancel)


# QUESTION 3
inline_btn_3_1 = InlineKeyboardButton(
    text='9',
    callback_data='9 inl btn',
)

inline_btn_3_2 = InlineKeyboardButton(
    text='10',
    callback_data='10 inl btn',
)

inline_btn_3_3 = InlineKeyboardButton(
    text='11',
    callback_data='11 inl btn',
)

inline_btn_3_4 = InlineKeyboardButton(
    text='12',
    callback_data='12 inl btn',
)

inline_keyboard_3 = InlineKeyboardMarkup().\
    row(inline_btn_3_1).\
    row(inline_btn_3_2).\
    row(inline_btn_3_3).\
    row(inline_btn_3_4).\
    row(inline_btn_cancel)


# QUESTION 4
inline_btn_4_1 = InlineKeyboardButton(
    text='13',
    callback_data='13 inl btn',
)

inline_btn_4_2 = InlineKeyboardButton(
    text='14',
    callback_data='14 inl btn',
)

inline_btn_4_3 = InlineKeyboardButton(
    text='15',
    callback_data='15 inl btn',
)

inline_btn_4_4 = InlineKeyboardButton(
    text='16',
    callback_data='16 inl btn',
)

inline_keyboard_4 = InlineKeyboardMarkup().\
    row(inline_btn_4_1).\
    row(inline_btn_4_2).\
    row(inline_btn_4_3).\
    row(inline_btn_4_4).\
    row(inline_btn_cancel)


# QUESTION 5
inline_btn_5_1 = InlineKeyboardButton(
    text='17',
    callback_data='17 inl btn',
)

inline_btn_5_2 = InlineKeyboardButton(
    text='18',
    callback_data='18 inl btn',
)

inline_btn_5_3 = InlineKeyboardButton(
    text='19',
    callback_data='19 inl btn',
)

inline_btn_5_4 = InlineKeyboardButton(
    text='20',
    callback_data='20 inl btn',
)

inline_keyboard_5 = InlineKeyboardMarkup().\
    row(inline_btn_5_1).\
    row(inline_btn_5_2).\
    row(inline_btn_5_3).\
    row(inline_btn_5_4).\
    row(inline_btn_cancel)
