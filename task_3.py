# Задача №3

import sys

with open('users.csv', 'r', encoding='cp1251') as file_1, \
        open('hobby.csv', 'r', encoding='cp1251') as file_2, \
        open('dict_users.txt', 'w', encoding='utf-8') as file_3:
    users = file_1.readlines()  # читаем файл построчно
    for users_line in users:  # если есть значения в файле пользователей
        hobby_line = file_2.readline().strip()
        if not hobby_line:  # если в хобби нет строк, то дополняем значением None
            hobby_line = None
        file_3.write(f'{users_line.strip()}: {hobby_line}\n')  # формируем в файл значения из 2-х файлов
    if file_2.readline():  # если в хобби остаются значения, а в пользователях - нет, то
