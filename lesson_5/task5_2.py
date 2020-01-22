"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("task5_2.txt", "r") as f:
        content = f.readlines()
except IOError:
    print("Произошла ошибка ввода-вывода!")
    quit()


print("Содержимое анализируемого файла:")
for line in content:
    print(line.rstrip('\n'))
print()
print("Анализ файла:")
print(f"Количество строк в файле: {len(content)}")
words_all = 0
for n, line in enumerate(content):
    s = line.rstrip('\n')
    words = len(s.split())
    print(f"Количество слов в строке № {n + 1}: {words}")
    words_all += words
print(f"Количество слов в файле: {words_all}")
