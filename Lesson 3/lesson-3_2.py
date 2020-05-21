def my_func(a, c, b, d, e):
    return (a + ' ' + b + ' ' + c + ' ' + d + ' ' + e)


name = input('Введите имя пользователя: ')
sur = input('Введите фамилию пользователя: ')
y = input('Город проживания: ')
m = input('E-mail: ')
t = input('Телефон: ')
print(my_func(a=name, b=sur, c=y, d=m, e=t))
