a = input('Введите значения списка через запятую: ')
a = (a.split(','))
for l in range(0, len(a) - 1, 2):
    a[l], a[l + 1] = a[l + 1], a[l]
print(a)
