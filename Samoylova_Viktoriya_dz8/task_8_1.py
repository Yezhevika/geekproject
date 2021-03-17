# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.

from re import compile

def email_parse(email):
    re_mail = compile(r"([\w]+)\@((?<=@)[^.]+\.\w+)")
    if re_mail.match(email):
        n, d = re_mail[0]
        print(dict(username=n, domain=d))
    else:
        raise ValueError

try:
    email_parse("samoylova.viktoriya.u@gmail.com")
    email_parse("samoylova.viktoriya.u@gmailcom")
except ValueError:
    print(f"Wromg email!")
