# срабатывает при извлечении элемента по индексу

# В этом примере описан класс Class2.
# В нём происходит заполнение списка my_list экземплярами класса Class1.
# Для получения элемента списка можно обратиться по индексу к элементу my_list

class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))


my_obj = Class2(10, True, "text")
print(my_obj.my_list[1])

# Теперь рассмотрим второй пример. Элемент извлекается по индексу не из атрибута экземпляра класса, а из самого объекта
# Во втором примере показано, как объекты пользовательского класса становятся
# похожими на объекты встроенных классов-последовательностей (строк, списков, кортежей)

class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
       return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __getitem__(self, index):
        return self.my_list[index]


my_obj = Class2(10, True, "text")
print(my_obj.my_list[0])
print(my_obj[1])
print(my_obj[2])
