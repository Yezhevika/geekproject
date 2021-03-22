# Реализовать класс Stationery (канцелярская принадлежность):
# 1) определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# 2) создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# 3) в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# 4) создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title} ")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")

stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("Copic")
marker.draw()
