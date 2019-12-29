"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    month = int(input("Введите номер месяца в виде целого числа от 1 до 12: "))
    if month in range(1, 13):
        break
    else:
        print("Номер введен некорректно - повторите ввод")

# наименования времен года закодируем, чтобы в случае переименования изменяли в одном месте а не во всем коде
# например в случае изменения языка вывода на английский меняем только здесь, а не в двух вариантах решения
winter = "зима"
spring = "весна"
summer = "лето"
autumn = "осень"

# реализация решения через list
list_month = [winter, winter, spring, spring, spring, summer, summer, summer, autumn, autumn, autumn, winter]
print(f"Номер месяца: {month} - время года: {list_month[month - 1]}")

# реализация решения через dict
dict_month = {
    1: winter,
    2: winter,
    3: spring,
    4: spring,
    5: spring,
    6: summer,
    7: summer,
    8: summer,
    9: autumn,
    10: autumn,
    11: autumn,
    12: winter
}
print(f"Номер месяца: {month} - время года: {dict_month[month]}")
