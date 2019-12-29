"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

# Создаем список
list_t = list()

# Заполняем его элементами различных типов данных
list_t.append("первый элемент")
list_t.append(2019)
list_t.append(3.14)
list_t.append([1, 2, 3])
list_t.append((1, 2, 3))
list_t.append({1, 2, 3})
list_t.append({1: 10, 2: 20, 3: 30})
list_t.append(True)
list_t.append(None)

print("Список для анализа: ", list_t)

# Определяем типы данных всех элементов в списке
print("Определяем типы данных всех элементов в списке:")
for i in list_t:
    print(f"type of {i} = {type(i)}")

# Cкрипт проверки типа данных каждого элемента
# Например, найдем элементы типа tuple и set
print("Ищем в скрипте элементы типа tuple и set:")
for i in list_t:
    if (type(i) == tuple) or (type(i) == set):  # PEP8 рекомендует здесь использовать isinstance()
        print(f"type of {i} = {type(i)}")
