import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher

from bot_settings import bot
from commands.question_buttons_commands_text import START_QUIZ_COMMAND, CANCEL_COMMAND

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
    NOT_NONE_STATE_CANCEL_COMMAND_TEXT,
    NONE_STATE_CANCEL_COMMAND_TEXT,
)


# -------------
# Quiz handlers
class CurrentQuestion(StatesGroup):
    """Класс для фиксации состояний ожидания ответа на определённый по счёту вопрос."""

    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()


# @disp.message_handler(commands=[f'{CANCEL_COMMAND}'], state='*')
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


# @disp.callback_query_handler(lambda cb: cb.data == f'/{CANCEL_COMMAND}', state='*')
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


# @disp.message_handler(commands=[f'{START_QUIZ_COMMAND}'], state='*')
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


# @disp.callback_query_handler(question_filter_1, state=CurrentQuestion.question_1)
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


# @disp.callback_query_handler(question_filter_2, state=CurrentQuestion.question_2)
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


# @disp.callback_query_handler(question_filter_3, state=CurrentQuestion.question_3)
async def process_question_3(callback_query: types.CallbackQuery):
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


# @disp.callback_query_handler(question_filter_4, state=CurrentQuestion.question_4)
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


# @disp.callback_query_handler(question_filter_5, state=CurrentQuestion.question_5)
async def process_question_5(callback_query: types.CallbackQuery, state: FSMContext):
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


# ---------------------
# Handlers registration
def register_static_command_handlers(disp: Dispatcher):
    disp.register_message_handler(
        cancel_command,
        commands=[f'{CANCEL_COMMAND}'],
        state='*',
    )
    disp.register_callback_query_handler(
        cancel_inline_button,
        # TODO: вынести этот фильтр в отдельную функцию
        lambda cb: cb.data == f'/{CANCEL_COMMAND}',
        state='*',
    )
    disp.register_message_handler(
        animal_command,
        commands=[f'{START_QUIZ_COMMAND}'],
        state='*',
    )
    disp.register_callback_query_handler(
        process_question_1,
        question_filter_1,
        state=CurrentQuestion.question_1,
    )
    disp.register_callback_query_handler(
        process_question_2,
        question_filter_2,
        state=CurrentQuestion.question_2,
    )
    disp.register_callback_query_handler(
        process_question_3,
        question_filter_3,
        state=CurrentQuestion.question_3,
    )
    disp.register_callback_query_handler(
        process_question_4,
        question_filter_4,
        state=CurrentQuestion.question_4,
    )
    disp.register_callback_query_handler(
        process_question_5,
        question_filter_5,
        state=CurrentQuestion.question_5,
    )
