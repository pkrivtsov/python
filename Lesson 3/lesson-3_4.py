# ------------first-------------------
def my_func(x, y):
    #    return (1 / pow(x, y))  # 1/(x**y)
# -----------second-------------------
    p = 1
    for number in range(y):
        p *= x
    return (1 / p)


x = abs(float(input('x= ')))
y = abs(int(input('y= ')))
print(my_func(x, y))
