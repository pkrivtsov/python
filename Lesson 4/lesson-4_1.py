from sys import argv

name, vir, st, prem = argv
try:
    print(f'Зарплата сотрудника: {int(vir) * int(st) + int(st) * int(prem) / 100:.2f} eur')
except ValueError:
    print("Вводить необходимо только числа!")
