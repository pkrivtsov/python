import numpy as np


class Matrix:
    def __init__(self, my_m):
        self.my_m = my_m

    def __add__(self, other):  # перегрузка метода
        try:
            return Matrix(np.array(self.my_m) + np.array(other.my_m))
        except ValueError:
            return 'Ошибка размерности матриц'

    def __str__(self):  # перегрузка метода
        return '\n'.join('\t'.join([str(el) for el in line]) for line in self.my_m)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_1 + matrix_2)
