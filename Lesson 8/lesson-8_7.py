class Complex_num:
    def __init__(self, num):
        self.num = complex(num)

    def __add__(self, other):
        return f'Sum = {self.num + other.num}'

    def __mul__(self, other):
        return f'Multuply = {self.num * other.num}'


c_1 = Complex_num('2+3j')
c_2 = Complex_num('3+7j')
print(c_1 + c_2, c_1 * c_2)
