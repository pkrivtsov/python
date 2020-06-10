class Car:  # создание базового класса
    def __init__(self, speed, color, name, is_police=False):  # конструктор
        self.speed = speed  # атрибуты класса
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):  # метод класса
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f"{self.name} turn on {'left' if direction == 'l' else 'right'}")

    def show_speed(self):
        return f'{self.name} going {self.speed} km/h'


class TownCar(Car):  # дочерние классы
    def show_speed(self):  # переопределение базового метода
        return f'{self.name} going {self.speed} km/h. Warning!!!' if self.speed > 60 else f'{self.name} going {self.speed} km/h'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} going {self.speed} km/h. Warning!!!' if self.speed > 40 else f'{self.name} going {self.speed} km/h'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):  # переопределение базового Car для работы с унаследованными атрибутами
        super().__init__(speed, color, name, is_police)





tc = TownCar(80, 'green', 'TownCar')
tc.go()
print(tc.color, tc.show_speed())
tc.turn('r')
tc.stop()

sc = SportCar(100, 'red', 'SportCar')
sc.go()
print(sc.color, sc.show_speed())
sc.turn('l')
sc.stop()

wc = WorkCar(35, 'grey', 'WorkCar')
wc.go()
print(wc.color, wc.show_speed())
wc.turn('l')
wc.stop()

pc = PoliceCar(50, 'blue', 'PoliceCar')
pc.go()
print(pc.color, pc.show_speed())
pc.turn('r')
pc.stop()
