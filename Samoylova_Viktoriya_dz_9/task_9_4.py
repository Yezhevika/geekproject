# # Реализуйте базовый класс Car:
# # 1) у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# # А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# # 2) опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# # 3) добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# # 4) для классов TownCar и WorkCar переопределите метод show_speed.
# # При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# #
# # Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# # Вызовите методы и покажите результат
#
# class Car:
#     "'Автомобиль'"
#
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f"Новая машина: {self.name} (цвет: {self.color}) полицейская машина - {self.is_police}")
#
#     def go(self):
#         print(f"{self.name}: Машина поехала")
#
#     def stop(self):
#         print(f"{self.name}: Машина остановилась")
#
#     def turn(self, direction):
#         print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}.")
#
#     def show_speed(self):
#         return f"{self.name}: Скорость автомобиля: {self.speed}."
#
# class TownCar(Car):
#     "'Городской автомобиль'"
#
#     def show_speed(self):
#         return f"{self.name}: Скорость автомобиля: {self.speed}. Повышение скорости" \
#             if self.speed() > 60 else f"{self.name}: Скорость автомобиля: {self.speed}."
#
#
# class WorkCar(Car):
#     "'Грузовой автомобиль'"
#
#     def show_speed(self):
#         return f"{self.name}: Скорость автомобиля: {self.speed}. Повышение скорости" \
#             if self.speed() > 40 else f"{self.name}: Скорость автомобиля: {self.speed}."
#
#
# class SportCar(Car):
#     "'Спортивный атомобиль'"
#
#
# class PoliceCar(Car):
#     "'Полицейская машина'"
#
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
#
# # police_car = PoliceCar('"Полицейская"', "белый", 80)
# # police_car.go()
# # print(police_car.show_speed())
# # police_car.tern(0)
# # police_car.stop()
# # print()
#
#
# work_car = WorkCar('"Грузовик"', "красный", 60)
# work_car.go()
# # work_car.tern(1)
# print(work_car.show_speed())
# # work_car.tern(0)
# work_car.stop()
#
# print()
# sport_car = SportCar('"Спотривная"', "зеленая", 130)
# sport_car.go()
# sport_car.tern(0)
# print(sport_car.show_speed())
# sport_car.stop()
#
# town_car = TownCar('"Городская"', "розовая", 60)
# town_car.go()
# town_car.tern(1)
# town_car.tern(0)
# print(town_car.show_speed())
# town_car.stop()
#
#
# print(f'\nМашина {town_car.name} (цвет{town_car.color})')
# print(f'\nМашина {sport_car.name} (цвет{sport_car.color})')
