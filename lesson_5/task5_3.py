"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

# Пытаемся прочитать файл
try:
    with open("task5_3.txt", "r", encoding='utf-8') as f:
        content = f.readlines()
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()

print("Содержимое анализируемого файла:")
for n, line in enumerate(content):
    s = line.rstrip('\n')
    print(f"Строка {n + 1}: {s}")

if not len(content):
    print(f"Ошибка: нет данных")
    quit()

# Записываем содержимое в словарь
# Вместе с этим проверяем структуру файла: в каждой строке минимум два значения, второе значение - число
data = {}
for n, line in enumerate(content):
    line_list = line.split()
    try:
        data[line_list[0]] = float(line_list[1])
    except IndexError:
        print(f"Ошибка в структуре данных: В строке {n + 1} должно быть минимум два значения!")
        quit()
    except ValueError:
        print(f"Ошибка в структуре данных: В строке {n + 1} второе значение должно быть числом!")
        quit()

# Определим, кто из сотрудников имеет оклад менее 20 тыс
print("Сотрудники, имеющие оклад менее 20 тыс:")
for k, v in data.items():
    if v < 20000:
        print(f"{k} {v}")

# Подсчет средней величины дохода сотрудников
joint_income = 0
for v in data.values():
    joint_income += v
average_income = joint_income / len(content)
print("Средняя величина дохода сотрудников = ", average_income)
