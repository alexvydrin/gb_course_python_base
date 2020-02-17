"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    # Формат даты при инициализации DD-MM-YYYY
    def __init__(self, str_date):
        self.str_date = None
        self.day, self.month, self.year = None, None, None
        day, month, year = Date.get_numbers_from_str(str_date)
        if isinstance(day, int):
            if Date.test_date(day, month, year):
                self.str_date = str_date
                self.day, self.month, self.year = day, month, year

    def __str__(self):
        if self.str_date:
            return self.str_date
        else:
            return "Дата неопределена"

    @classmethod
    def get_numbers_from_str(cls, str_date):
        try:
            day = int(str_date[:2])
            month = int(str_date[3:5])
            year = int(str_date[6:])
            return day, month, year
        except ValueError:
            print(f"Ошибка: формат даты должен быть DD-MM-YYYY (указан {str_date})")
            return None, None, None

    @staticmethod
    def test_date(day, month, year):
        if day < 1 or day > 31:
            print("Ошибка: День должен быть в интервале 1-31")
            return False
        if month < 1 or month > 12:
            print("Ошибка: Месяц должен быть в интервале 1-12")
            return False
        if year < 1900 or year > 2100:
            print("Ошибка: Год должен быть в интервале 1900-2100")
            return False
        return True


# test 1
d = Date('10-12-2005')
print("Дата:", d)
print("День:", d.day)
print("Месяц:", d.month)
print("Год:", d.year)

# test 2
d = Date('xx-12-2005')
print("Дата:", d)
print("День:", d.day)
print("Месяц:", d.month)
print("Год:", d.year)

# test 3
d = Date('-1-12-2005')
print("Дата:", d)
print("День:", d.day)
print("Месяц:", d.month)
print("Год:", d.year)
