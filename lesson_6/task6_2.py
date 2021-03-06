"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*
число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    __mass = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
    __depth = 5  # толщина полотна в сантиметрах

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_mass(self):
        return self._length * self._width * Road.__mass * Road.__depth


road_1 = Road(5000, 20)
mass = road_1.calculation_mass()
print(f"Масса асфальта = {mass} кг. ({mass/1000} т.)")
