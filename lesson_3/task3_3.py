"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(value_1, value_2, value_3):
    return value_1 + value_2 + value_3 - min(value_1, value_2, value_3)


print(my_func(0, 2, 4))
