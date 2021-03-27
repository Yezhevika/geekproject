# Выполним перегрузку конструктора. Конструктор класса отвечает за создание объекта класса.

class MyClass:
    def __init__(self, param):
        self.param = param


mc = MyClass("text")
print(mc.param)
