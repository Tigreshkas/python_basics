# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt


def select_information(string):
    """get a list of tuples of the form:
    (<remote_addr>, <request_type>, <requested_resource>)
    from a file string"""
    info_1 = string.split(' ')[0]  # разделяем строку по пробелам и берем 0-й элемент
    info_2 = string.split('"')[1].split(' ')[0]  # разделяем строку по кавычкам и 1-й элемент разбиваем по пробелам,
    # берем от этого 0-й элемент
    info_3 = string.split('"')[1].split(' ')[1]  # разделяем строку по кавычкам и 1-й элемент разбиваем по пробелам,
    # берем от этого 1-й элемент
    info_tuple = (info_1, info_2, info_3)  # в результате получаем кортеж, который выводим в результате выполнения ф-ции
    return info_tuple


with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:  # открываем файл с данными и работаем на чтение
    with open('my_file.txt', 'w', encoding='utf-8') as f:  # создаем (пересоздаем) файл с необходимыми записями
        row = file_1.readlines()  # разбиваем файл на строки
        for line in row:  # читаем файл построчно
            print(select_information(line))  # выводим в консоль результаты выполнения функции
            print(select_information(line), file=f)  # а также записываем эти результаты в новый файл (т.к. исходный
            # файл слишком большой и не все результаты выводятся в консоль, зато в файле выводятся все необходимые
            # результаты.
