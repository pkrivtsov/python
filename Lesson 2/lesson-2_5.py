my_list = [7, 5, 3, 3, 2]
my_list.reverse()
a = int(input('Введите элеметн рейтинга: '))
if a in my_list:
    my_list.insert(my_list.index(a), a)
else:
    my_list.append(a)
my_list.reverse()
print(my_list)
