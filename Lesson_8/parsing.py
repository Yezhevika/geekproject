# Попробуем при помощи регулярного выражения найти все даты в тексте

# import re
#
# RE_DATE = re.compile(r'(?:\d{2}[./-]){2}\d{4}')
#
# txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. ' \
#      'Надеемся, что 24-01-2021 будет без ветра.'
#
# print(RE_DATE.findall(txt))
#  ------------------------------------------------
# есть текст с данными о товарах пользователя.
# Известно, что название товара обёрнуто в кавычки, а его цена идет после названия в круглых скобках
# (между ними может быть пробел, табуляция или даже несколько пробелов).
# Нужно получить список кортежей вида (<название товара>, <цена>)

# import re
#
# RE_PRODUCTS = re.compile(r'"([^"]+)"\s*\((\d+(?:[,.]\d+)*).*\)')
#
# txt = '''
# Иван сегодня сделал заказ: "iPhone 12"  (158900,6 руб),
# "Galaxy S21"(98653.7 р).
# Позже он добавил в корзину "iPad"\t(32451)
# '''
#
# print(RE_PRODUCTS.findall(txt))

# ------------------------------------------------------
# найти в тексте слова, которые начинаются и заканчиваются на одну и ту же букву

# import re
#
# RE_EQ_LETTERS = re.compile(r'\b(\w)\w*\1\b')
#
# txt = 'Однако, хорошо у вас получилось. А как еще могло быть?'
#
# print(RE_EQ_LETTERS.findall(txt))
# print(RE_EQ_LETTERS.search(txt))
# print(RE_EQ_LETTERS.match(txt))
# print(*RE_EQ_LETTERS.finditer(txt))
#
# -------------------------------------------------------
# распарсить GET-данные в URL адресе в именованные группы

import re

RE_GET_PARSER = re.compile(r'(?<=[&?])(?P<key>[^&]+)=(?P<val>[^&]+)(?=&*)')

url = 'https://translate.google.com/?hl=ru&sl=en&tl=ru&text=go&op=translate'

print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(url)), sep=', ')
