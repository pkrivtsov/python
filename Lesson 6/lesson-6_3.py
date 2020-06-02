class Worker:  # создание  класса родитель
    def __init__(self, name, surname, position, wage, bonus):  # конструктор
        self.name = name  # атрибуты класса
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):  # создание  класса наследник
    def get_full_name(self):  # метод класса, наследующего все атрибуты Worker
        return f'{self.name} {self.surname}'

    def total_income(self):
        return f'{sum(self._income.values())}'


# создание экземпляра класса Position
w = Position('Vasily', 'Pupkin', 'Developer', 10000, 2000)
# проверяем значение атрибута
print(w.position)
# выводим методы экземпляра
print(w.get_full_name())
print(w.total_income())
