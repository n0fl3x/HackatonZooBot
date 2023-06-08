import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv, find_dotenv

from keyboards.about_kb import about_inline_keyboard
from keyboards.contacts_kb import zoo_contacts_inline_keyboard
from urls import MSK_ZOO_START_LOGO_LINK
from commands.question_buttons_commands_text import START_QUIZ_COMMAND, CANCEL_COMMAND

from commands.static_commands import (
    START_COMMAND,
    HELP_COMMAND,
    ABOUT_COMMAND,
    CONTACTS_COMMAND,
    CREATORS_COMMAND,
)

from handler_filters import (
    question_filter_1,
    question_filter_2,
    question_filter_3,
    question_filter_4,
    question_filter_5,
)

from texts.questions_text import (
    QUESTION_1,
    QUESTION_2,
    QUESTION_3,
    QUESTION_4,
    QUESTION_5,
    END_MESSAGE,
)

from keyboards.questions_kb import (
    inline_keyboard_1,
    inline_keyboard_2,
    inline_keyboard_3,
    inline_keyboard_4,
    inline_keyboard_5,
)

from texts.static_commands_text import (
    START_COMMAND_TEXT,
    HELP_COMMAND_TEXT,
    CONTACTS_COMMAND_TEXT,
    ABOUT_COMMAND_TEXT,
    CREATORS_COMMAND_TEXT,
    NOT_NONE_STATE_CANCEL_COMMAND_TEXT,
    NONE_STATE_CANCEL_COMMAND_TEXT,
)


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


# ---------------
# Static commands

@dp.message_handler(commands=[f'{START_COMMAND}'], state='*')
async def start_command(message: types.Message) -> None:
    await message.answer_photo(
        photo=MSK_ZOO_START_LOGO_LINK,
        caption=START_COMMAND_TEXT
    )


@dp.message_handler(commands=[f'{HELP_COMMAND}'], state='*')
async def help_command(message: types.Message) -> None:
    await message.answer(text=HELP_COMMAND_TEXT)


@dp.message_handler(commands=[f'{ABOUT_COMMAND}'], state='*')
async def about_command(message: types.Message) -> None:
    await message.answer(
        text=ABOUT_COMMAND_TEXT,
        reply_markup=about_inline_keyboard
    )


@dp.message_handler(commands=[f'{CONTACTS_COMMAND}'], state='*')
async def contacts_command(message: types.Message) -> None:
    await message.answer(
        text=CONTACTS_COMMAND_TEXT,
        reply_markup=zoo_contacts_inline_keyboard
    )


@dp.message_handler(commands=[f'{CREATORS_COMMAND}'], state='*')
async def contacts_command(message: types.Message) -> None:
    await message.answer(text=CREATORS_COMMAND_TEXT)


# -----------------
# Question handlers

class CurrentQuestion(StatesGroup):
    """Класс для фиксации состояний ожидания ответа на определённый по счёту вопрос."""

    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()


@dp.message_handler(commands=[f'{CANCEL_COMMAND}'], state='*')
async def cancel_command(message: types.Message, state: FSMContext) -> None:
    """Функция-обработчик команды /cancel, введённой вручную. Останавливает текущий опрос."""

    current_state = await state.get_state()

    if current_state is None:
        logging.info(f'User with ID {message.from_user.id} tried to cancel empty state.')
        await message.answer(text=NONE_STATE_CANCEL_COMMAND_TEXT)
        return

    logging.info(f'User with ID {message.from_user.id} cancelled quiz at {current_state} state by command.')
    await state.finish()
    await message.answer(text=NOT_NONE_STATE_CANCEL_COMMAND_TEXT)


@dp.callback_query_handler(lambda cb: cb.data == f'/{CANCEL_COMMAND}', state='*')
async def cancel_inline_button(callback: types.CallbackQuery, state: FSMContext) -> None:
    """Функция-обработчик команды /cancel, вызванная через инлайн-кнопку. Останавливает текущий опрос."""

    current_state = await state.get_state()

    if current_state is None:
        logging.info(f'User with ID {callback.from_user.id} tried to cancel empty state.')
        await callback.answer()
        await callback.message.answer(text=NONE_STATE_CANCEL_COMMAND_TEXT)
        return

    logging.info(f'User with ID {callback.from_user.id} cancelled quiz at {current_state} state by inline button.')
    await state.finish()
    await callback.answer()
    await callback.message.answer(text=NOT_NONE_STATE_CANCEL_COMMAND_TEXT)


@dp.message_handler(commands=[f'{START_QUIZ_COMMAND}'], state='*')
async def animal_command(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state is None:
        logging.info(f'User with ID {message.from_user.id} started new quiz.')
    else:
        await message.answer(text='Вы начали опрос заново.')
        logging.info(f'User with ID {message.from_user.id} restarted quiz.')

    await message.answer(
        text=QUESTION_1,
        reply_markup=inline_keyboard_1
    )
    await CurrentQuestion.question_1.set()


@dp.callback_query_handler(question_filter_1, state=CurrentQuestion.question_1)
async def process_question_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data
    )
    await CurrentQuestion.next()
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=QUESTION_2,
        reply_markup=inline_keyboard_2,
    )


@dp.callback_query_handler(question_filter_2, state=CurrentQuestion.question_2)
async def process_question_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data
    )
    await CurrentQuestion.next()
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=QUESTION_3,
        reply_markup=inline_keyboard_3,
    )


@dp.callback_query_handler(question_filter_3, state=CurrentQuestion.question_3)
async def process_question_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data
    )
    await CurrentQuestion.next()
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=QUESTION_4,
        reply_markup=inline_keyboard_4,
    )


@dp.callback_query_handler(question_filter_4, state=CurrentQuestion.question_4)
async def process_question_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data
    )
    await CurrentQuestion.next()
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=QUESTION_5,
        reply_markup=inline_keyboard_5,
    )


@dp.callback_query_handler(question_filter_5, state=CurrentQuestion.question_5)
async def process_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data
    )
    await state.finish()
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=END_MESSAGE,
    )


# -------
# Run bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
