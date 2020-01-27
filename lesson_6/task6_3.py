"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы:
- получение полного имени сотрудника (get_full_name)
- получение дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname):
        # Атрибуты name и surname задаем при создании объекта
        self.name = name
        self.surname = surname
        # Остальные атрибуты будут задаваться с помощью специальных методов
        self.position = None
        self._income = {"wage": None, "bonus": None}

    def determine_position(self, position, wage, bonus):
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


# Проверяем работу примера на реальных данных

# 1.Создаем экземпляры класса Position
person_1 = Position("Иван", "Сидоров")
person_2 = Position("Василий", "Кузнецов")

# 2.Передаем данные
person_1.determine_position("Дворник", 10000, 2000)
person_2.determine_position("Электрик", 30000, 5000)

# 3.Проверяем значения атрибутов
print(f"Должность: {person_1.position} Фамилия: {person_1.surname}")
print(f"Должность: {person_2.position} Фамилия: {person_2.surname}")

# 4.Вызываем методы экземпляров
print(f"Сотрудник {person_1.get_full_name()} зарабатывает {person_1.get_total_income()} рублей")
print(f"Сотрудник {person_2.get_full_name()} зарабатывает {person_2.get_total_income()} рублей")
