def my_func(a, b, c):
    num = [a, b, c]
    return (sum(num) - min(num))


k = int(input('a= '))
l = int(input('b= '))
m = int(input('c= '))
print(my_func(k, l, m))
