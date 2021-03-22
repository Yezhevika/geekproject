class Auto:
    def __init__(self):
        print("Автомобиль заведен")
        self.auto_name = "Mazda" # публичная переменная (без _ нижнего подчеркивания перед именем переменной)
        self._auto_year = 2019   # защищенная (с 1 _)
        self.__auto_model = "CX9" # приватная переменная (с 2 __)
a = Auto()
print(a.auto_name)
