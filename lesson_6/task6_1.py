"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:

    # настройка продолжительности состояний светофора
    __duration_red = 7
    __duration_yellow = 2
    __duration_green = 7

    def __init__(self):
        self.__color = "flashing yellow"  # сигнал, что светофор пока не запущен

    def change_color(self, new_color, duration):
        self.__color = new_color
        print("На светофоре горит цвет:", self.__color)
        sleep(duration)

    def running(self, number_of_cycles=-1):
        """
        number_of_cycles - количество циклов работы светофора
        если параметр равен -1 или не указан, то светофор будет работать вечно
        """
        print("Начало работы светофора")
        number_left = number_of_cycles
        while number_left:
            self.change_color("red", TrafficLight.__duration_red)
            self.change_color("yellow", TrafficLight.__duration_yellow)
            self.change_color("green", TrafficLight.__duration_green)
            self.change_color("yellow", TrafficLight.__duration_yellow)
            if number_left > 0:
                number_left -= 1
        print("Окончание работы светофора")
        self.__color = "flashing yellow"  # сигнал, что светофор пока не запущен


tl = TrafficLight()
tl.running(2)
