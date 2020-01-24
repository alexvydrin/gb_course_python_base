"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# Пытаемся прочитать файл
try:
    with open("task5_4.txt", "r", encoding='utf-8') as f:
        content = f.readlines()
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()

print("Содержимое исходного файла:")
for n, line in enumerate(content):
    s = line.rstrip('\n')
    print(f"Строка {n + 1}: {s}")

if not len(content):
    print(f"Ошибка: нет данных")
    quit()

# Записываем содержимое в список
# Вместе с этим проверяем структуру файла: в каждой строке минимум два значения, разделенных любым знаком, например "-"
data = []
for n, line in enumerate(content):
    line_list = line.split()
    try:
        data.append([line_list[0], line_list[2]])
    except IndexError:
        print(f"Ошибка в структуре данных: В строке {n + 1} должно быть минимум два значения, разделенных любым знаком"
              f" (например тире) и пробелами!")
        quit()

# Словарь для перевода
translator = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}

# Переводим
data_out = []
for word, value in data:
    try:
        data_out.append([translator[word.lower()], value])
    except KeyError:
        print(f"Не могу найти перевод для {word}")

# Записываем в новый файл
print("Содержимое нового файла:")
try:
    with open("task5_4_out.txt", "w", encoding='utf-8') as f:
        for word, value in data_out:
            s = f"{word.capitalize()} - {value}"
            print(s)
            f.write(s+'\n')

except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()
