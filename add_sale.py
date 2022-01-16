# Собираем вводимые значения в файл (задача 6)
import sys

try:  # обрабатываем ошибку (если файл не существует, создаем его)
    file = open('bakery.csv', 'r')
except FileNotFoundError:
    file = open('bakery.csv', 'w')
    file.close()

with open('bakery.csv', 'r+', encoding='utf=8') as file_1:
    row = file_1.readlines()
    i = 0
    for _ in row:  # счетчик строк
        i += 1
    print(f'{i + 1}: {sys.argv[1]}', file=file_1)  # запись строки в файл
