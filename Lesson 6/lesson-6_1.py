from itertools import cycle
from time import sleep
from termcolor import colored  # pip install


class TrafficLight:  # создание класса
    __color = {"red": 7, "yellow": 2, "green": 7}  # приватный атрибут класса

    def running(self):  # метод класса
        for i in cycle(self.__color):
            print(colored(i, i))  # текст, цвет
            sleep(self.__color.get(i))


t = TrafficLight()  # создание объекта (экземпляра класса)
t.running()  # запуск метода класса
