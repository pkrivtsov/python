class Storage:
    """Склад оргтехники"""
    stor = {}
    comp = {}

    def add_product(self, product, count, price):
        self.stor[product.name] = {'Количество': count, 'Цена': price}

    def transfer(self, product):
        for key in list(self.stor.keys()):
            if key == product.name:
                self.comp[product.name] = self.stor.get(product.name)
                del self.stor[key]


class Equipment:
    """Оргтехника"""
    name = ''
    eq = 'шт'

    def __str__(self):
        return self.name


class Printer(Equipment):
    name = 'Принтер'

    def __init__(self, p_name, is_color=True):
        self.name = f'{self.name} {p_name}'
        self.is_color = is_color


class Scaner(Equipment):
    name = 'Сканер'

    def __init__(self, s_name, type):  # ручной, страничный, планшетный
        self.name = f'{self.name} {s_name}'
        self.type = type


class Xerox(Equipment):
    name = 'Ксерокс'

    def __init__(self, x_name, mfu=False):  # отдельный, МФУ
        self.name = f'{self.name} {x_name}'
        self.mfu = mfu


def int_dry():
    while True:
        try:
            n = int(input('Сколько единиц добавим?: '))
        except ValueError:
            print(f'Только число')
        else:
            return n


storage = Storage()
# ---------------------добавляем принтеры----------------------------
p = input('Введите, через пробел, название принтера, цену и тип (1-цв., 0-ч/б): ').split()
printer_1 = Printer(p[0], bool(p[2]))
storage.add_product(printer_1, int_dry(), int(p[1]))
# --------------------добавляем сканеры--------------------------------
s = input('Введите, через пробел, название сканера, цену и тип (ручной, страничный, планшетный): ').split()
scaner_1 = Scaner(s[0], s[2])
storage.add_product(scaner_1, int_dry(), int(s[1]))
# --------------------добавляем ксероксы--------------------------------
x = input('Введите, через пробел, название ксерокса, цену и тип (1-МФУ, 0-отдельный): ').split()
xerox_1 = Xerox(x[0], bool(x[2]))
storage.add_product(xerox_1, int_dry(), int(x[1]))
# ---------------------состояние склада--------------------------------
print(f'На складе:\n{storage.stor}')
# ---------------------перемещение в отдел-----------------------------
t = int(input(f'Что передадим в отдел компании?\n1-{printer_1} 2-{scaner_1} 3-{xerox_1}: '))
if t == 1:
    storage.transfer(printer_1)
elif t == 2:
    storage.transfer(scaner_1)
else:
    storage.transfer(xerox_1)
# -------------------состояния склада и отдела--------------------------
print(f'На складе:\n{storage.stor}')
print(f'В отделе:\n{storage.comp}')
