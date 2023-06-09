import logging

from aiogram import executor

from bot_settings import dp

from handlers import (
    quiz_handlers,
    static_command_handlers,
)


# --------
# Starting
async def on_startup(dp):
    logging.info(' Bot is active.')


# --------
# Handlers
quiz_handlers.register_static_command_handlers(disp=dp)
static_command_handlers.register_static_command_handlers(disp=dp)


# ---------
# Finishing
async def on_shutdown(dp):
    logging.warning(' Shutting down...')


# -------
# RUN BOT
if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
