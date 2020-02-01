"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def material_size(self):
        pass


class Coat(Clothes):

    @property
    def material_size(self):
        # self.value - V - размер
        return round((self.value / 6.5 + 0.5), 2)


class Suit(Clothes):

    @property
    def material_size(self):
        # self.value - H - рост
        return round(2 * self.value + 0.3, 2)


coat_1 = Coat(13)
print(f"Расход ткани для пальто (размер V = {coat_1.value}) = {coat_1.material_size}")
suit_1 = Suit(13)
print(f"Расход ткани для костюма (рост H = {suit_1.value}) = {suit_1.material_size}")

print("Суммарный расход ткани на производство одежды = ", coat_1.material_size + suit_1.material_size)
