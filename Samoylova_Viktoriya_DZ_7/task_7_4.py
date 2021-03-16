# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0)

import os
import django
from collections import defaultdict

def dir_info():
    root_dir = django.__path__[0] # используем файловую структуру библиотеки django
    django_files = defaultdict(int) # используем помошника создания справочника
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size)) # длинна числа в 10 степени
            django_files[size] += 1 # суммируем количество
        for size, nums in sorted(django_files.items()): # выводим в отсортированном порядке
            print(f'{size}: {nums}')

dir_info()
