class Auto:
    # атрибуты класса
    auto_name = "Lexus"
    auto_model = "RX 350L"
    auto_year = 2019

    # методы класса
    def on_auto_start(self):
        print(f"Заводим автомобиль")

    def on_auto_stop(self):
        print(f"Останавливаем работу двигателя")

a = Auto()           # создаётся экземпляр класса Auto, ссылка на который связывается с переменной a
print(a)             # Содержимое переменной a
print(type(a))       # проверяется тип переменной a — это класс Auto
print(a.auto_name)   # осуществляется получение доступа к одному из атрибутов класса
a.on_auto_start()    # запуск методов класса
a.on_auto_stop()     # запуск методов класса

