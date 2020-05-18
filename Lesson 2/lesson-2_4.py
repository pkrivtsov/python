a = input('Введите слова через пробел: ')
a = (a.split(' '))
for l in a:
    print(a.index(l), l[:10])
