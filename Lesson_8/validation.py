# пользователь должен ввести своё имя с большой буквы, допустимы только русские буквы (тут 2 решения)

# import re
#
# RE_NAME = re.compile(r'^[А-ЯЁ][а-яё]+$')
#
#
# def name_is_valid(name):
#    return RE_NAME.match(name)
#
# # valid_letters = {chr(sym_code) for sym_code in range(ord('а'), ord('я') + 1)}
# # valid_letters.add('ё')
# #
# # def name_is_valid(name):
# #    if not name or set(name.lower()) - set(valid_letters):
# #        return False
# #    return name.istitle()
#
# if __name__ == '__main__':
#    while True:
#        name = input('Введите имя:\n')
#        if name_is_valid(name):
#            break
#    print(f'пользователь: {name}')
# ------------------------------------------------
# Попробуем написать «регулярку» для валидации даты в формате «ДД.ММ.ГГГГ»:

import re
RE_DATE = re.compile(r'^(\d{2}\.){2}\d{4}$')
for date in ['23.01.2021', '23,01,2021', '23~01~2021']:
    assert RE_DATE.match(date), f'wrong date {date}' # специально указана ошибка AssertionError: wrong date 23,01,2021