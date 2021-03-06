# Задание 5
"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = float(input("Введите размер выручки фирмы: "))
costs = float(input("Введите размер издержек фирмы: "))
profit = revenue - costs
if profit > 0:
    print(f"Прибыль фирмы равняется {profit}")
    print(f"Рентабельность равняется {profit / revenue * 100}%")
    staff = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника равняется {profit / staff}")
elif profit < 0:
    print(f"Убыток фирмы равняется {-profit}")
else:
    print(f"Прибыль фирмы нулевая")
