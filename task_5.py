# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
import random


def get_jokes(quantity, repeat):
    """Create n jokes of three random words"""
    nouns_copy = nouns.copy()
    adverbs_copy = adverbs.copy()
    adjectives_copy = adjectives.copy()
    new_jokes = []  # создаем новый список
    if repeat == '+':  # проверяем, если слова в шутках могут повторяться:
        while quantity > 0:  # пока количество шуток > 0:
            for i in range(quantity):  # перебираем количество шуток
                new_jokes.append(random.choice(nouns_copy) + ' ' + random.choice(adverbs_copy) +
                                 ' ' + random.choice(adjectives_copy))  # в новый список вносим рандомное слово
                # из трёх списков
            quantity = - 1
    else:  # проверяем, если слова в шутках не могут повторяться:
        while quantity > 0:
            for i in range(quantity):
                word_1 = random.choice(nouns_copy)  # создаем копии списков, чтобы потом была возможность
                word_2 = random.choice(adverbs_copy)  # удалять использованные слова из списков
                word_3 = random.choice(adjectives_copy)
                new_jokes.append(word_1 + ' ' + word_2 + ' ' + word_3)  # в новый список вносим рандомное слово
                nouns_copy.remove(f'{word_1}')  # удаляем из копии списков слова, использованные в шутках
                adverbs_copy.remove(f'{word_2}')
                adjectives_copy.remove(f'{word_3}')
            quantity = - 1
    return new_jokes  # возвращаем список с шутками


quantity_jokes = int(input('Введите количество шуток: '))
word_repeated = input('Слова в шутках повторяются? +/- ')
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
if quantity_jokes > 5 and word_repeated == '-':  # если слова в шутках не должны повторяться и шуток больше 5, то
    print('Количество шуток с неповторяющимися словами должно быть меньше 5.')  # выводим данный результат
else:  # если слова в шутках могут повторяться, то
    print(get_jokes(quantity_jokes, word_repeated))  # выводим полученные шутки
