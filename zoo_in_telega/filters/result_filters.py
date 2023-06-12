from random import choice

from texts.answer_buttons_text import *
from database.all_animals import ALL_ANIMALS


async def get_totem_animal(proxy_dict: dict) -> dict:
    hidden_results = {}

    qualities = []
    for animal in ALL_ANIMALS.values():
        for qual in animal['ANIMAL_QUALITIES']:
            qualities.append(qual)

    quals_set = set(qualities)
    for item in quals_set:
        hidden_results[item] = 0

    chat_id = proxy_dict.get('user_id')

    # ------------
    # 1st question
    if proxy_dict['1st_question'] == answer_1_1:
        hidden_results['скорость'] += 1
        hidden_results['безбашенность'] += 1
    if proxy_dict['1st_question'] == answer_1_2:
        hidden_results['скрытность'] += 1
        hidden_results['спокойствие'] += 1
    if proxy_dict['1st_question'] == answer_1_3:
        hidden_results['теплолюбивость'] += 1
        hidden_results['неуклюжесть'] += 1
    if proxy_dict['1st_question'] == answer_1_4:
        hidden_results['редкость'] += 1
        hidden_results['стадность'] += 1

    # ------------
    # 2nd question
    if proxy_dict['2nd_question'] == answer_2_1:
        hidden_results['теплолюбивость'] += 1
        hidden_results['спокойствие'] += 1
    if proxy_dict['2nd_question'] == answer_2_2:
        hidden_results['скорость'] += 1
        hidden_results['скрытность'] += 1
    if proxy_dict['2nd_question'] == answer_2_3:
        hidden_results['одиночка'] += 1
        hidden_results['безбашенность'] += 1
    if proxy_dict['2nd_question'] == answer_2_4:
        hidden_results['храбрость'] += 1
        hidden_results['стадность'] += 1

    # ------------
    # 3rd question
    if proxy_dict['3rd_question'] == answer_3_1:
        hidden_results['скорость'] += 1
        hidden_results['безбашенность'] += 1
    if proxy_dict['3rd_question'] == answer_3_2:
        hidden_results['редкость'] += 1
        hidden_results['ловкость'] += 1
    if proxy_dict['3rd_question'] == answer_3_3:
        hidden_results['теплолюбивость'] += 1
        hidden_results['одиночка'] += 1
    if proxy_dict['3rd_question'] == answer_3_4:
        hidden_results['скрытность'] += 1
        hidden_results['спокойствие'] += 1

    # ------------
    # 4th question
    if proxy_dict['4th_question'] == answer_4_1:
        hidden_results['неуклюжесть'] += 1
        hidden_results['стадность'] += 1
    if proxy_dict['4th_question'] == answer_4_2:
        hidden_results['одиночка'] += 1
        hidden_results['скорость'] += 1
    if proxy_dict['4th_question'] == answer_4_3:
        hidden_results['спокойствие'] += 1
        hidden_results['скрытность'] += 1
    if proxy_dict['4th_question'] == answer_4_4:
        hidden_results['храбрость'] += 1
        hidden_results['безбашенность'] += 1

    # ------------
    # 5th question
    if proxy_dict['5th_question'] == answer_5_1:
        hidden_results['теплолюбивость'] += 1
        hidden_results['скрытность'] += 1
    if proxy_dict['5th_question'] == answer_5_2:
        hidden_results['спокойствие'] += 1
        hidden_results['одиночка'] += 1
    if proxy_dict['5th_question'] == answer_5_3:
        hidden_results['скорость'] += 1
        hidden_results['ловкость'] += 1

    # это кнопка про бинтуронга
    if proxy_dict['5th_question'] == answer_5_4:
        return {
            'chat_id': chat_id,
            'photo': ALL_ANIMALS['ANIMAL_1']['ANIMAL_IMAGE'],
            'caption': ALL_ANIMALS['ANIMAL_1']['ANIMAL_DESCRIPTION'],
            'reply_markup': ALL_ANIMALS['ANIMAL_1']['ANIMAL_KB'],
        }

    proxy_dict.pop('user_id')
    max_value = max(hidden_results.values())

    final_dict = {key: value for key, value in hidden_results.items() if value == max_value}
    top_qualities_list = [q for q in final_dict.keys()]

    filtered_animals = []
    for quality in top_qualities_list:
        for animal in ALL_ANIMALS.values():
            for anim in animal['ANIMAL_QUALITIES']:
                if quality == anim:
                    filtered_animals.append(animal['ANIMAL_NAME'])

    animal_to_get = []

    if len(filtered_animals) == 1:
        for animal, dict_ in ALL_ANIMALS.items():
            for v in dict_.values():
                if v == filtered_animals[0]:
                    animal_to_get.append(animal)

        return {
            'chat_id': chat_id,
            'photo': ALL_ANIMALS[f'{animal_to_get[0]}']['ANIMAL_IMAGE'],
            'caption': ALL_ANIMALS[f'{animal_to_get[0]}']['ANIMAL_DESCRIPTION'],
            'reply_markup': ALL_ANIMALS[f'{animal_to_get[0]}']['ANIMAL_KB'],
        }

    else:
        for animal, dict_ in ALL_ANIMALS.items():
            for v in dict_.values():
                if v == filtered_animals[0]:
                    animal_to_get.append(animal)

        my_animal = choice(animal_to_get)

        return {
            'chat_id': chat_id,
            'photo': ALL_ANIMALS[f'{my_animal}']['ANIMAL_IMAGE'],
            'caption': ALL_ANIMALS[f'{my_animal}']['ANIMAL_DESCRIPTION'],
            'reply_markup': ALL_ANIMALS[f'{my_animal}']['ANIMAL_KB'],
        }
