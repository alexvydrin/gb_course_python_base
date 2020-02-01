"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnErrorZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Выполним операцию деления")
value1 = input("Введите делимое: ")
value2 = input("Введите делитель: ")

try:
    value1 = float(value1)
    value2 = float(value2)
    if not value2:
        raise OwnErrorZeroDivision("Делитель не может быть равен 0!")
    result = value1 / value2
except ValueError:
    print("Вы ввели не число")
except OwnErrorZeroDivision as err:
    print(err)
else:
    print(f"Результат = {round(result, 3)}")
