# Написать декоратор для логирования типов позиционных аргументов функции
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции

def type_logger(func):
    def wrapper(*args, **kwargs):
        n = [f"{func.__name__}({type(el)})" for el in args] + \
            [f"{func.__name__}({type(kwargs[el])})" for el in kwargs]
        print(*n, sep=",\n")

    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5, [11, 22], False, "DFGHJ", ui=89.8)
