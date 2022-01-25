# Задание 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates.

import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
html_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(html_dir):  # если нет папки templates в папке my_project, то создаем её
    os.makedirs(html_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):  # если какая-либо папка содержит папку templates, то
        for folder in dirs:
            if not os.path.exists(os.path.join(html_dir, folder)):
                os.makedirs(os.path.join(html_dir, folder))
        for file in files:
            src_file = os.path.join(root, file)
            html_file = os.path.join(html_dir, os.path.basename(root))
            if not os.path.dirname(src_file) == html_file:
                shutil.copy(src_file, html_file)
