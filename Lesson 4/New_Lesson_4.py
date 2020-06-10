#  -------------------------------------------------------- 1 ----------------------------------------------------------


from sys import argv


def salary():
    try:
        time, stavka, premia = map(int, argv[1:])
        print(f"Salary - {time * stavka + premia}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#  -------------------------------------------------------- 3 ----------------------------------------------------------


uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

#  -------------------------------------------------------- 4 ----------------------------------------------------------


from random import randint

my_list = [randint(-10, 10) for i in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

#  -------------------------------------------------------- 6 ----------------------------------------------------------


from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print(
    'Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода'
    ' из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        #  repeat_list = [next(cycle(my_list)) for el in range(num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"


print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import count, cycle

progr_lang = list(input("Введите через пробел ТОП 5 языков программирования: ").split())

# создаем бесконечный итератор из списка языков программирования введенным пользователем
iter = cycle(progr_lang)

# выводим с помощью итератора count с ограничением, чтобы не уйти в бесконечный цикл
for n in count():
    if n > 10:
        break
    else:
        print(f"{n} - {next(iter)}")


#  -------------------------------------------------------- 7 ----------------------------------------------------------

from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)


generator = fact_gen()
x = 0
for i in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


def fact_gen(n):
    m = 1
    for i in range(1, n):
        if i > 15:
            break
        m *= i
        yield m


for i in fact_gen(26):
    print(i)
