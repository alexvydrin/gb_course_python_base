"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open("task5_1.txt", "w") as f:
    n = 1  # Номер вводимой строки
    while True:
        new_string = input(f"Введите строку № {n} для записи в файл (пустая строка - окончание ввода): ")
        if not new_string:
            break
        f.write(new_string + '\n')
        n += 1

print("Ввод окончен. Содержимое файла:")
with open("task5_1.txt", "r") as f:
    for line in f:
        print(line.rstrip('\n'))