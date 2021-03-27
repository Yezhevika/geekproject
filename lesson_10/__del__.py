# В Python разработчик может участвовать как в создании, так и в удалении объекта.

class MyClass:
    def __init__(self, param):
        self.param = param

    def __del__(self):
        print(f"Удаляем объект {self.param} класса MyClass")


mc = MyClass("text")
del mc
