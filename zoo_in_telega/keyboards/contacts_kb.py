from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from texts.static_commands_buttons_text import CONTACTS_BUTTON_TEXT
from urls.static_commands_urls import ZOO_CONTACTS_URL


zoo_contacts_btn = InlineKeyboardButton(
    text=CONTACTS_BUTTON_TEXT,
    url=ZOO_CONTACTS_URL,
)

zoo_contacts_inline_keyboard = InlineKeyboardMarkup().add(zoo_contacts_btn)
