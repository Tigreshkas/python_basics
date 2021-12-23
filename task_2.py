# Задание 2. Работа со списком.

word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
new_word = []

i = 0
while i < len(word_list):
    object_list = word_list[i]
    object_number = object_list[1:]  # присваиваем переменной срез строки (все, кроме первого символа) из списка
    if object_list[0] == '-':  # проверяем, если первый элемент строки из списка равен "-" или "+"
        word_list[i] = str('-' + f'{object_number.zfill(2)}')  # присваиваем строке из списка значение числа с "-" и 00
    elif object_list[0] == '+':
        word_list[i] = str('+' + f'{object_number.zfill(2)}')  # присваиваем строке из списка значение числа с "+" и 00

    if not word_list[i].isalpha():  # если строка из списка не является набором символов (т.е. является числом), то:
        new_word.append('"')  # в новый список вставляем кавычки,
        new_word.append(word_list[i].zfill(2))  # затем число
        new_word.append('"')  # затем ещё кавычки
    else:  # если строка является набором символов, то:
        new_word.append(word_list[i])  # просто добавляем в новый список значение
    i += 1
print(new_word)

word_str = ' '.join(new_word)  # собираем список в строку через пробел
print(word_str)
