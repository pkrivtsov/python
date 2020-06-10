#  -------------------------------------------------------- 1 ----------------------------------------------------------


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return round(div_num, 4)


print(div(input("Enter first number - "), input("Enter second - ")))

#  -------------------------------------------------------- 2 ----------------------------------------------------------


def personal_info(**kwargs):
    return kwargs


print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
      birthday=input("Enter your birthday: "), city=input("Enter your city: "), email=input("Enter your email: "),
      phone_number=input("Enter your phone number: ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def person_inf(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city};" \
           f" email - {email}; phone - {phone}"


print(person_inf(name="Alice", surname="Selezneva", birthday="21.09.67", city="Moscow",
                 email="alice.selezneva@mail.ru", phone="143-91-19 "))

#  -------------------------------------------------------- 3 ----------------------------------------------------------


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "Enter only a numbers!"


print(my_func(2, 11, -30))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_func(1978, 1, 2))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)

print(my_func(8, 7, 9))

#  -------------------------------------------------------- 4 ----------------------------------------------------------

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res


print(my_pow_fun(4.5, -2))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода данных:\nх должен быть больше 0\ny должен быть меньше 0'
        else:
            result = 1
            for i in range(abs(y)):
                result *= 1 / x
            return f'Результат возведения x в степень y: {round(result, 6)}'
    except ValueError:
        return "Программа работает только с числами."


number1 = input('Введите действительное положительное число, x = ')
number2 = input('Введите целое отрицательное число, y = ')

print(my_func2(number1, number2))


#  ------------------------------------------- вариант решения ---------------------------------------------------------
#  рекурсия


def i_involve_r(x, y):
    return 1 if y == 0 else i_involve_r(x, y + 1) * 1 / x


a = 2  # должно быть: действительное положительное число x
b = -4  # должно быть: целое отрицательное число y

print(f"Solved via recursion  {a} raised to power {b} = {i_involve_r(a, b)}")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input 'q' to exit: ").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("To exit the program, enter - 'q'.")
        print(f"Sum of numbers = {s}")


print(sum_num())

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def summary():
    result = 0
    while True:
        print(f"Текущая сумма = {result}")
        input_s = input("Введите строку чисел, разделенных пробелом для подсчета суммы (# - символ для завершения): ").split()
        for value in input_s:
            if value == "#":
                print(f"Окончательная сумма = {result}")
                break
            try:
                result += float(value)
            except ValueError:
                print(f"Значение {value} не было учтено при подсчете суммы - неверный тип")
        else:
            # если символа завершения программы не были то продолжаем ввод данных
            continue
        # сюда мы дойдем только если встретим символ завершения программы
        break
    return f"Окончательная сумма = {result}"

summary()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


num = 0
try:
    while num != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split()):
            num += i
        print(num)
except ValueError:
    print(num)

#  -------------------------------------------------------- 6 ----------------------------------------------------------


def int_func(words):
    # function takes words(split by space) and uppercase first letter in any words
    # verify that the all letters its lower latin script and spaces
    for i in words:
        if not ord(i) == 32 and not 97 <= ord(i) <= 122:
            print("Lower latin script and spaces between!\n")
            words = input("Enter words with a space(lower latin script):\n")
            break
    words_list = words.split()
    for i in range(len(words_list)):
        print(words_list[i][0].upper() + words_list[i][1:], end=" ")


int_func(input("Enter words with a space(lower latin script):\n"))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def int_func(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result

print(int_func(input("Введите строку: ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


int_func = lambda sentence: print(sentence.title())

int_func(input("Please enter set of words. "))
