# class Auto:
#     def on_start(self):
#         info = "Автомобиль заведен" # создаётся локальная переменная info в рамках метода on_start() класса Auto
#         return info
#
# a = Auto()
# print(a.info) # Появится ошибка, потому что нельзя получить доступ к локальной переменной info

class Auto:
   info_1 = "Автомобиль заведён" #создаётся глобальная переменная info_1,на экран выводится её значение. И ошибка не возникает

   def on_start(self):
       info_2 = "Автомобиль заведён"
       return info_2

a = Auto()
print(a.info_1)
