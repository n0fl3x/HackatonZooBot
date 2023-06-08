from aiogram import executor

from bot_settings import dp

from handlers import (
    quiz_handlers,
    static_command_handlers,
)


# --------
# Starting
async def on_startup(_):
    print('Bot is online.')


# --------
# Handlers
quiz_handlers.register_static_command_handlers(disp=dp)
static_command_handlers.register_static_command_handlers(disp=dp)


# -------
# Run bot
if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
