class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __str__(self):  # преобразует объект к строке
        return self.num

    def __add__(self, other):  # срабатывает при участии объекта в операции сложения в качестве операнда с левой стороны
        return f'Sum={self.num + other.num}'

    def __sub__(self, other):
        return self.num - other.num if self.num - other.num > 0 else 'subtraction impossible'

    def __mul__(self, other):
        return f'Multiply={self.num * other.num}'

    def __truediv__(self, other):
        return f'Truediv={round(self.num / other.num)}'

    def make_order(self, line):
        return '\n'.join(['*' * line for _ in range(self.num // line)]) + '\n' + '*' * (self.num % line)


cell_1 = Cell(23)
cell_2 = Cell(13)
print(cell_1.make_order(4))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
