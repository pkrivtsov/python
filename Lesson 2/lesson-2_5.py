my_list = [7, 5, 3, 3, 2]
l = len(my_list)
a = int(input('Введите элемент рейтинга: '))
if a in my_list:
    my_list.insert(my_list.index(a) + my_list.count(a), a)
else:
    for idx, sym in enumerate(my_list):
        if a > sym:
            my_list.insert(idx, a)
            break
if len(my_list) == l: my_list.append(a)
print(my_list)
