class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def __init__(self): # классе реализован конструктор, увеличивающий значение auto_count на единицу и выводящий на экран итоговое значение
        Auto.auto_count += 1
        print(Auto.auto_count)

a_1 = Auto()
a_2 = Auto()
a_3 = Auto()
