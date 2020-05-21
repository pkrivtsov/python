def my_func(m):
    return (sum(m))


s = 0
keep = True
while keep:

    num = input('Числа через пробел или 111 - завершить: ').split()
    for i, item in enumerate(num):
        if num[i].isdigit() and num[i] != "111":
            num[i] = int(item)

        elif not num[i].isdigit():
            print(f'значение {num[i]} должно быть числом')
            num[i] = 0
        else:
            num[i:] = []
            keep = False

    s += my_func(num)
    print(s)
