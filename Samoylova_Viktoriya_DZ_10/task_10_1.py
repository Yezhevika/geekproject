# Реализовать класс Matrix(матрица).Обеспечить перегрузку конструктора класса(метод
# __init__()), который должен принимать данные(список списков) для формирования матрицы.

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j] )


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix_1 + matrix_2\n{matrix_1 + matrix_2}")

