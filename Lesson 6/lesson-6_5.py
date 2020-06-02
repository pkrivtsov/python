class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}-pen'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}-pencil'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}-handle'


s = Stationery()
print(s.draw())
p = Pen('Microsoft')
print(p.draw())
pl = Pencil('Apple')
print(pl.draw())
h = Handle('Stabilo')
print(h.draw())
