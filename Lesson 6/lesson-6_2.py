class Road:  # создание класса
    def __init__(self, length=10, width=10):  # конструктор (спец. метод, вызываемый при создании экземпляра класса)
        self._length = length  # защищенные атрибуты класса
        self._width = width

    def mass(self, thick=1):  # метод класса
        self.thick = thick
        m = self._length * self._width * thick * 25
        return m


r = Road(5000, 20)  # создание объекта (экземпляра класса) с атрибутами
print(f'Масса асфальта: {r.mass(5) / 1000}т')  # запуск метода класса с атрибутом
