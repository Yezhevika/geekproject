# ключевые принципы ООП: инкапсуляцией, наследованием и полиморфизмом.
# ИНКАПСУЛЯЦИЯ - это механизма сокрытия данных
# НАСЛЕДОВАНИЕ - некоторым объектом характеристик другого объекта-родителя.
# Объект называется дочерним и обладает не только характеристиками родителя, но и собственными свойствами.
# Благодаря наследованию можно избежать дублирования кода.


# class MyClass:
#     _attr = "значение" # Одиночное подчёркивание в начале имени атрибута или метода свидетельствует о том, что атрибут или методы не предназначены для использования вне класса
#     def _method(self):
#         print("Это защищенный метод!")
#
# mc = MyClass()
# mc._method()
# print(mc._attr)

# class MyClass:
#     __attr = "значение" # Использование двойного подчёркивания перед именем атрибута и метода делает их недоступными по этому имени.
#     def __method(self):
#         print("Это защищенный метод!")
#
# mc = MyClass()
# mc.__method()
# print(mc.__attr)

# class MyClass:
#     __attr = "значение"
#     def __method(self):
#         print("Это защищённый метод!")
#
# mc = MyClass()
# mc._MyClass__method() # Обратиться к атрибуту или методу по-прежнему можно, используя следующий подход: _ИмяКласса__ИмяАтрибута.
# print(mc._MyClass__attr)

# НАСЛЕДОВАНИЕ:
# Класс Transport
# class Transport:
#     def transport_method(self):
#         print("Это родительский метод из класса Transport")
#
# class Auto(Transport):  # Класс Auto, наследующий Transport (наследник)
#     def auto_method(self):
#         print("Это метод из дочернего класса")
#
# a = Auto()
# a.transport_method()

# Несколько дочерних классов у одного родителя
# класс Transport
class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
# class Auto(Transport):
#     def auto_method(self):
#         print("Дочерний метод класса Auto")
#
# # класс Bus, наследующий Transport
# class Bus(Transport):
#     def bus_method(self):
#         print("Дочерний метод класса Bus")
#
# a = Auto()
# a.transport_method()
# b = Bus()
# b.transport_method()

# Рассмотрим ещё один пример, в котором класс-родитель Shape определяет атрибуты.
# Эти атрибуты могут быть характерны для всех классов-наследников.
# Например, цвет фигуры, ширина и высота, основание и высота.
# Здесь в конструкторах классов-наследников инициализируются параметры.
# Часть их — собственные атрибуты классов-наследников, а некоторые наследуются от родителей.
# Чтобы работать с унаследованными атрибутами, нужно их перечислить, например, super().__init__(color, param_1, param_2).
# Тем самым мы показываем, что хотим иметь возможность работы с атрибутами класса-родителя.
# Если атрибуты не перечислить, то при попытке обращения к ним через экземпляр класса-наследника возникнет ошибка.
# class Shape:
#     def __init__(self, color, param_1, param_2):
#         self.color = color
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     def square(self):
#         return self.param_1 * self.param_2
#
# class Rectangle(Shape):
#     def __init__(self, color, param_1, param_2, rectangle_p):
#         super().__init__(color, param_1, param_2)
#         self.rectangle_p = rectangle_p
#
#     def get_r_p(self):
#         return self.rectangle_p
#
#
# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#
#     def get_t_p(self):
#         return self.triangle_p
#
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())

# Несколько родителей у одного класса

# class Player:
#     def player_method(self):
#         print("Родительский метод класса Player")
#
# class Navigator:
#     def navigator_method(self):
#         print("Родительский метод класса Navigator")
#
# class MobilePhone(Player, Navigator):
#     def mobile_phone_method(self):
#         print("Дочерний метод класса MobilePhone")
#
# m_p = MobilePhone()
# m_p.player_method()
# m_p.navigator_method()

# Возможна ситуация, когда у классов-родителей совпадают имена атрибутов и методов.
# Тогда обращение к такому атрибуту или методу через «наследник» будет адресовано к атрибуту или методу того
# класса-родителя, который значится первым.

class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"

class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"


class Triangle(Shape, Material):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)
        pass

t = Triangle(10, 20)
print(t.get_params())