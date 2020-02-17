"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Warehouse:

    def __init__(self, number):
        self.number = number
        self.list = []

    def __str__(self):
        return f"Склад № {self.number}"

    def add_item(self, obj, count):
        # Проверяем тип count
        if not isinstance(count, int):
            print(f"Не могу оприходовать на {self}: оргтехника {obj} в количестве {count} шт - "
                  f"исправьте тип у количества")
            return

        for i in self.list:
            if i["item"] == obj:
                i["count"] += count
                break
        else:
            self.list.append({"item": obj, "count": count})
        print(f"Оприходование на {self}: оргтехника {obj} в количестве {count} шт")

    def sub_item(self, obj, count, department):
        # Проверяем тип count
        if not isinstance(count, int):
            print(f"Не могу сделать перемещение из {self} в {department}: оргтехника {obj} в количестве {count} шт - "
                  f"исправьте тип у количества")
            return

        # выясним, есть ли такой предмет на складе и достаточное ли его количество
        for i in self.list:
            if i["item"] == obj and i["count"] >= count:
                i["count"] -= count
                print(f"Перемещение из {self} в {department}: оргтехника {obj} в количестве {count} шт")
                break
        else:
            print(f"Данная позиция отсутствует на складе в требуемом количестве ({obj} в количестве {count} шт)")

    def show_list(self):
        print("Содержимое склада:")
        for n, i in enumerate(self.list):
            print(f"{n + 1}: {i['item']} = {i['count']} шт.")


class OfficeEquipment:
    type = 'оргтехника'

    def __init__(self, model, price):
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    type = 'принтер'

    def __init__(self, model, price, info_printer):
        super().__init__(model, price)
        self.info_printer = info_printer

    def __str__(self):
        return f"{self.type} {self.model} ({self.info_printer})"


class Scanner(OfficeEquipment):
    type = 'сканер'

    def __init__(self, model, price, info_scanner):
        super().__init__(model, price)
        self.info_scanner = info_scanner

    def __str__(self):
        return f"{self.type} {self.model} ({self.info_scanner})"


class Copier(OfficeEquipment):
    type = 'ксерокс'

    def __init__(self, model, price, info_copier):
        super().__init__(model, price)
        self.info_copier = info_copier

    def __str__(self):
        return f"{self.type} {self.model} ({self.info_copier})"


# Создаем склад
warehouse = Warehouse(1)

# Создаем примеры номенклатуры
printer_1 = Printer("model_1", 1000, "black")
scanner_1 = Scanner("model_2", 2000, "thin")
copier_1 = Copier("model_3", 3000, "very big")

print(warehouse)

# Тестируем добавление
warehouse.add_item(printer_1, 5)
warehouse.add_item(scanner_1, 10)
warehouse.add_item(copier_1, 15)
# Тестируем добавление если уже есть на складе
warehouse.add_item(scanner_1, 2)
# Тестируем ошибку типа
warehouse.add_item(scanner_1, "два")

warehouse.show_list()

# Тестируем удаление
warehouse.sub_item(scanner_1, 3, "отдел кадров")

# Тестируем удаление если нет на складе
warehouse.sub_item(scanner_1, 300, "отдел кадров")
# Тестируем ошибку типа
warehouse.sub_item(printer_1, "три штуки", "отдел кадров")

warehouse.show_list()
