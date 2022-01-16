# Функция для вывода необходимых данных (задача 6)
import sys


def all_sale(num_min, num_max):
    """A generator that returns a value for the required number"""
    with open('bakery.csv', 'r', encoding='utf=8') as file_2:
        row = file_2.readlines()
        for line_str in row:
            if num_min <= int(line_str.split(':')[0]) <= num_max:
                yield line_str.split(':')[1]


try:  # обрабатываем ошибку (если файл не существует, создаем его)
    file = open('bakery.csv', 'r')
except FileNotFoundError:
    file = open('bakery.csv', 'w')
    file.close()

line = 0  # счетчит строк в файле
with open('bakery.csv', 'r', encoding='utf=8') as file_1:
    lines = file_1.readlines()
    line += 1

if len(sys.argv) == 3:  # если 3 аргумента, то выводим от одного значения до другого
    print(*all_sale(int(sys.argv[1]), int(sys.argv[2])))
elif len(sys.argv) == 2:  # если 2 аргумента, то выводим от одного значения до конца
    print(*all_sale(int(sys.argv[1]), line))
elif len(sys.argv) == 1:  # если 1 аргумент, то выводим все значения
    print(*all_sale(1, line))
else:
    print('Введены неверные параметры.')
