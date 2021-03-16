# Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом
# редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os

def make_dir():
    with open("config.yaml", "r", encoding="utf-8") as f:
        for line in f:
            *path_list, last_path = line.strip().split(",") # отделяем последний элемент от остальных
            if last_path.find(".") < 0: # если нет расширения, то это каталог
                path_list.append(last_path) # добавляем его в список
            if not os.path.exists(os.path.join(*path_list)): # если нет такого каталога, то создаем
                os.makedirs(os.path.join(*path_list))
            if last_path.find(".") > 0: # если есть точка - это расширение, файл создаем его
                with open(os.path.join(*path_list, last_path), "w", encoding="utf-8") as new_f:
                    new_f.write("")

if __name__ == "__main__":
    make_dir()


