# Задание 4

import os

root_dir = os.path.dirname(__file__)
dir_path = os.path.join(root_dir, 'my_project')
stat_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for root, dirs, files in os.walk(root_dir):  # перебираем всё
    for file in files:  # перебираем каждый файл в папке
        file_size = os.stat(os.path.join(root, file)).st_size  # узнаем размер файла
        if 0 <= file_size <= 100:  # циклы для подсчета:
            stat_dict[100] += 1
        if 100 < file_size <= 1000:
            stat_dict[1000] += 1
        if 1000 < file_size <= 10000:
            stat_dict[10000] += 1
        if file_size > 10000:
            stat_dict[100000] += 1

print(stat_dict)
