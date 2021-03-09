# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
# формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobbies.csv", "r", encoding="utf-8") as hobby:

        all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): (el[1]).strip() for el in all_list}

        with open(dict_n_h.json, "w", encoding="utf-8") as f:
            if "None" in my_dict:
                print(1)
            else:
                dump(my_dict, f, ensure_ascii=False, indent=4)
                print(my_dict)
