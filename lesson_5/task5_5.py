"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from random import randint

# Создаем текстовый файл и записываем в него программно набор чисел, разделенных пробелами.
with open("task5_5.txt", "w") as f:
    for i in range(10):
        f.write(f"{randint(1, 99)} ")

# Читаем получившийся файл
try:
    with open("task5_5.txt", "r") as f:
        content = f.read()
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()

print("Содержимое анализируемого файла:")
print(content)

# Подсчитываем сумму чисел в файле и выводим ее на экран
sum_values = 0
for i in content.split():
    sum_values += int(i)
print("Сумма чисел:", sum_values)
