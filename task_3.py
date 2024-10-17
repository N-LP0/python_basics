Класс-исключение должен контролировать типы данных элементов списка.
"""

class NumErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        a = input("Введите значения: ")
        if a == "p":
            break
        if a.isnumeric() == True:
            my_list.append(a)
        else:
            raise NumErr("Введено не число")
        print(my_list)
    except NumErr as err:
        print(err)
