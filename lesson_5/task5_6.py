"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# Пытаемся прочитать файл
try:
    with open("task5_6.txt", "r", encoding='utf-8') as f:
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

# На основании данных формируем словарь
# Вместе с этим проверяем структуру файла:
# количество занятий записывается как тире или как число после которого сразу идет условное обозначение:
# (л),(пр) или (лаб)

data = {}
for n, line in enumerate(content):
    line_list = line.split()
    cnt = 0
    for v in line_list[1:]:
        try:
            if v == "-":
                pass
            elif v.find("(л)") != -1:
                cnt += float(v[:v.find("(л)")])
            elif v.find("(пр)") != -1:
                cnt += float(v[:v.find("(пр)")])
            elif v.find("(лаб)") != -1:
                cnt += float(v[:v.find("(лаб)")])
            else:
                cnt += float(v)
        except ValueError:
            print(f"Ошибка в структуре данных: В строке {n + 1} не могу расшифровать значение {v} "
                  f"(количество занятий записывается как тире или как число после которого сразу идет "
                  f"условное обозначение: (л),(пр) или (лаб)")

        data[line_list[0]] = cnt

print("Сформированный словарь:")
print(data)