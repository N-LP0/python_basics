Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))

try:
    if b == 0:
        raise ZeroErr("НА ноль делить нельзя ")
except ZeroErr as err:
    print(err)
else:
    print(a / b)
