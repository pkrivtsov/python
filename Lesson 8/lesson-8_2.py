class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input('Введите делимое и делитель через пробел: ').split()
try:
    if int(inp_data[1]) == 0:
        raise OwnError('Error: Division by zero')
except IndexError:
    print('Error: Only 2 numbers')
except ValueError:
    print('Error: Not a number')
except OwnError as err:
    print(err)
else:
    print(int(inp_data[0]) / int(inp_data[1]))
