Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class MyWarehouse(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, name, cost, quantity, number_of_lists):
        self.name = name
        self.price = cost
        self.numb = number_of_lists
        try:
            if isinstance(quantity, int):

                self.quantity = quantity

                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyWarehouse("Введите число!!!")

        except MyWarehouse as text:
            print(text.txt)


class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier  {self.numb} times'


Printer_1 = Printer('Brother', 7400, 12, 10)
Scanner_1 = Scanner('Xerox', 12500, 3, 8)
Warehouse.reception(Printer_1)
Warehouse.reception(Scanner_1)

print(Warehouse.goods)

print(Scanner_1.to_scan())
