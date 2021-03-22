# Реализовать базовый класс Worker (работник):
# 1) определить атрибуты: name, surname, position (должность), income (доход);
# 2) последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# 3) создать класс Position (должность) на базе класса Worker;
# 4) в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# 5) проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

meneger = Position("Dorian", "Grey", "CEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())
