"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    # a + bi

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        a = self.a
        b = self.b
        z = "+"
        if b < 0:
            b = -b
            z = "-"
        if b == 1:
            b = ""
        return f"{a} {z} {b}i"

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        # (a + bi) · (c + di) = ac + bci + adi + bdi2 = (ac - bd) + (bc + ad)i
        a = self.a * other.a - self.b * other.b
        b = self.b * other.a + self.a * other.b
        return ComplexNumber(a, b)


value_1 = ComplexNumber(2, 3)
value_2 = ComplexNumber(5, -7)
print(value_1)
print(value_2)
print("Результат сложения:", value_1 + value_2)
print("Результат произведения:", value_1 * value_2)
