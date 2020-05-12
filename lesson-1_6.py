a = float(input("a= "))
b = float(input("b= "))
t = 1
while a < b:
    a += a * .1
    t += 1
print('на', t, '-й день спортсмен достиг результата — не менее', b, 'км.')
