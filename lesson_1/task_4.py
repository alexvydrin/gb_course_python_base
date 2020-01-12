# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_input = input("Введите любое целое положительное число, программа определит самую большую цифру в нем: ")
# предполагаем что пользователь ввел действительно целое положительное число, проверку ввода не далаем
number_temp = int(number_input)  # это значение будем изменять в процессе анализа исходного числа
number_max = 0  # предполагаем что самая большая цифра в числе равна 0 (меньше не будет точно)
while number_temp > 0:
    number_next = number_temp % 10  # определеяем очередную цифру в числе для анализа
    if number_next > number_max:
        number_max = number_next  # нашли новый максимум
    number_temp = number_temp // 10  # переходим к следующей цифре в числе
print(f"В числе {number_input} самая большая цифра = {number_max}")