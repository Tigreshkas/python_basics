# Задание 1. Написать скрипт, создающий стартер (заготовку) для проекта:

import os


def create_dir(name_1):
    """"Функция проверки существования папки и создания её в случае отсутствия"""
    dir_add = name_1
    if not os.path.exists(dir_add):
        os.mkdir(dir_add)


def create_subfolder(dir_1, dir_2):
    """Функция проверки существования вложенной папки и создания её в случае отсутствия"""
    dir_path = os.path.join(dir_1, dir_2)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    create_dir('my_project')  # создание основной папки
    create_subfolder('my_project', 'settings')  # создание вложенных папок
    create_subfolder('my_project', 'mainapp')
    create_subfolder('my_project', 'adminapp')
    create_subfolder('my_project', 'authapp')
