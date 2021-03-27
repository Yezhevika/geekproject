# срабатывает при обращении к экземпляру класса как к функции

class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, newparam):
        self.param = newparam

    def __str__(self):
        return f"Значение параметра - {self.param};"


obj_1 = MyClass("width")
obj_2 = MyClass("height")

obj_1("length")
obj_2("square")

print(obj_1, obj_2)
