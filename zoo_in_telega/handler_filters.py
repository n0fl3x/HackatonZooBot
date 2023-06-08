from aiogram import types


param_1 = 10
param_2 = 10


async def question_filter_1(callback_query: types.CallbackQuery):
    global param_1
    global param_2

    if callback_query.data == '1 inl btn':
        param_1 += 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '1 вариант'
        return callback_query

    if callback_query.data == '2 inl btn':
        param_1 -= 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '2 вариант'
        return callback_query

    if callback_query.data == '3 inl btn':
        param_1 += 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '3 вариант'
        return callback_query

    if callback_query.data == '4 inl btn':
        param_1 -= 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '4 вариант'
        return callback_query

    if callback_query.data == '/cancel':
        return callback_query


async def question_filter_2(callback_query: types.CallbackQuery):
    global param_1
    global param_2

    if callback_query.data == '5 inl btn':
        param_1 += 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '5 вариант'
        return callback_query

    if callback_query.data == '6 inl btn':
        param_1 -= 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '6 вариант'
        return callback_query

    if callback_query.data == '7 inl btn':
        param_1 += 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '7 вариант'
        return callback_query

    if callback_query.data == '8 inl btn':
        param_1 -= 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '8 вариант'
        return callback_query

    if callback_query.data == '/cancel':
        return callback_query


async def question_filter_3(callback_query: types.CallbackQuery):
    global param_1
    global param_2

    if callback_query.data == '9 inl btn':
        param_1 += 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '9 вариант'
        return callback_query

    if callback_query.data == '10 inl btn':
        param_1 -= 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '10 вариант'
        return callback_query

    if callback_query.data == '11 inl btn':
        param_1 += 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '11 вариант'
        return callback_query

    if callback_query.data == '12 inl btn':
        param_1 -= 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '12 вариант'
        return callback_query

    if callback_query.data == '/cancel':
        return callback_query


async def question_filter_4(callback_query: types.CallbackQuery):
    global param_1
    global param_2

    if callback_query.data == '13 inl btn':
        param_1 += 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '13 вариант'
        return callback_query

    if callback_query.data == '14 inl btn':
        param_1 -= 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '14 вариант'
        return callback_query

    if callback_query.data == '15 inl btn':
        param_1 += 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '15 вариант'
        return callback_query

    if callback_query.data == '16 inl btn':
        param_1 -= 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '16 вариант'
        return callback_query

    if callback_query.data == '/cancel':
        return callback_query


async def question_filter_5(callback_query: types.CallbackQuery):
    global param_1
    global param_2

    if callback_query.data == '17 inl btn':
        param_1 += 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '17 вариант'
        return callback_query

    if callback_query.data == '18 inl btn':
        param_1 -= 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '18 вариант'
        return callback_query

    if callback_query.data == '19 inl btn':
        param_1 += 1
        param_2 += 1
        print(param_1, param_2)
        callback_query.data = '19 вариант'
        return callback_query

    if callback_query.data == '20 inl btn':
        param_1 -= 1
        param_2 -= 1
        print(param_1, param_2)
        callback_query.data = '20 вариант'
        return callback_query

    if callback_query.data == '/cancel':
        return callback_query
