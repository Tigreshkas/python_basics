# Функция, переводящая числительные от 0 до 10 с англ. на русский язык с учетом регистра

def num_translate(key):
    """ Function for translate number """
    if key.istitle() is True:  # если слово введено с большой буквы, то выводим результат с большой буквы
        print(number_translation[key.lower()].capitalize())
    else:  # если слово введено с маленькой буквы, то выводим результат с маленькой буквы
        print(number_translation[key])


number_user = input('Введите число на английском языке (от 0 до 10): ')
number_translation = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
# храним словарь не в функции, т.к. будем в дальнейшем обращаться к этому словарю
if number_user.lower() in number_translation:  # проверка наличия введенного числа в словаре
    num_translate(number_user)  # есть в словаре - выводим перевод(с учетом регистра)
else:
    print(None)  # нет в словаре - выводим "None"
