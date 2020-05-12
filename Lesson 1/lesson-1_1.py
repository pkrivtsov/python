a = 25.5
b = int(a) + 5
c = bool(b)
print('a=', a, type(a), 'b=', b, type(b), 'c=', c, type(c))
b = ' Vasily'
c = input('What is the surname of Vasily? ')
c += b
a = int(input('How old is ' + c + "? "))
print('Name: ', c, 'Age: ', a)
