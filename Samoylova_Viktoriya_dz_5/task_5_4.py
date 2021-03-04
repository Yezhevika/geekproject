# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего

from random import randrange

src = range(0, 50, 3)

# src = [300, 3, 4, 5, 6, 7, 8, 2]

rezult = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
print(rezult)
