def my_func(a, b):
    try:
        return (int(a) / int(b))
    except ZeroDivisionError:
        return ("Делить на 0 в поле дейтсвительных (вещественных) чисел нельзя!")
    except ValueError:
        return ("Вводить необходимо только числа!")


a = input("Введите число а: ")
b = input("Введите число b: ")
print(my_func(a, b))
