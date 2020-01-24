"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.type_car = ""  # Тип автомобиля не определен - тип будем определять в подклассах

    def go(self):
        print(f"{self.color} {self.type_car} {self.name} поехал")

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.type_car} {self.name} остановился")

    def turn(self, direction):
        print(f"{self.color} {self.type_car} {self.name} повернул {direction}")

    def set_speed(self, speed):
        self.speed = speed

    def show_speed(self):
        print(f"{self.color} {self.type_car} {self.name} движется со скоростью {self.speed} км/час")


class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type_car = "городской автомобиль"

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Внимание! Автомобиль превысил скорость!")


class SportCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type_car = "спортивный автомобиль"


class WorkCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type_car = "рабочий автомобиль"

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Внимание! Автомобиль превысил скорость!")


class PoliceCar(Car):

    is_police = True

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type_car = "полицейский автомобиль"


car_t = TownCar("номер аа111а", "Красный")
print(f"Появился {car_t.type_car} {car_t.name}, его цвет {car_t.color.lower()}")  # доступ к атрибутам
print("Этот автомобиль является полицейским:", car_t.is_police)
car_t.go()
car_t.set_speed(60)
car_t.set_speed(70)
car_t.show_speed()
car_t.turn("налево")
car_t.stop()

car_s = SportCar("номер bb222b", "Синий")
print(f"Появился {car_s.type_car} {car_s.name}, его цвет {car_s.color.lower()}")  # доступ к атрибутам
print("Этот автомобиль является полицейским:", car_s.is_police)
car_s.go()
car_s.set_speed(80)
car_s.show_speed()
car_s.turn("направо")
car_s.stop()

car_w = WorkCar("номер cc333c", "Зеленый")
print(f"Появился {car_w.type_car} {car_w.name}, его цвет {car_w.color.lower()}")  # доступ к атрибутам
print("Этот автомобиль является полицейским:", car_w.is_police)
car_w.go()
car_w.set_speed(100)
car_w.show_speed()
car_w.turn("налево")
car_w.stop()

car_p = PoliceCar("номер xx444x", "Желтый")
print(f"Появился {car_p.type_car} {car_p.name}, его цвет {car_p.color.lower()}")  # доступ к атрибутам
print("Этот автомобиль является полицейским:", car_p.is_police)
car_p.go()
car_p.set_speed(120)
car_p.show_speed()
car_p.turn("направо")
car_p.stop()
