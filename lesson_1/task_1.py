# Задание 1
# Поработайте с переменными, создайте несколько,
# выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

number_1 = 450
number_2 = 4.5
number_res = number_1 + number_2
print(f"Сумма чисел {number_1} и {number_2} равняется {number_res}")
print(f"Тип результата: {type(number_res)}")
number_1 = int(input("Введите целое число: "))
number_2 = float(input("Введите дробное число: "))
string_1 = input("Введите первую строку: ")
string_2 = input("Введите вторую строку: ")
print(f"Вы ввели числа {number_1} и {number_2}")
print(f"Вы ввели строки '{string_1}' и '{string_2}'")