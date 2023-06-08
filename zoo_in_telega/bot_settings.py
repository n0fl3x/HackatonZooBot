import logging
import os

from dotenv import load_dotenv, find_dotenv

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# ------------
# Bot settings
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()


bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

dp = Dispatcher(
    bot=bot,
    storage=storage
)
