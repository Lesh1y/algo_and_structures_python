"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
from functools import reduce

# Решение с использованием встроенных функций
NUMS = defaultdict(list)
for i in range(2):
    n = input(f'Введите {i+1}-е натуральное шестнадцатиричное число: ')
    NUMS['%s-%s' % (i + 1, n)] = list(n)
print(NUMS)

MY_SUM = sum([int(''.join(j), 16) for j in NUMS.values()])
print(f'Сумма: {list("%X" % MY_SUM)}')

PRODUCT = reduce(lambda a, b: a *
                 b, [int(''.join(j), 16) for j in NUMS.values()])
print(f'Произведение: {list("%X" % PRODUCT)}')


# Через ООП


class HexOperation:
    """Перегрузка стандартных сложения и умножения"""

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) +
                        int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) *
                        int(''.join(other.second_num), 16)))[2:]


FIRST_HEX_NUM = list(input('Введите первое шестнадцатиричное число: '))
SECOND_HEX_NUM = list(input('Введите второе шестнадцатиричное число: '))

RESULT_SUM = HexOperation(FIRST_HEX_NUM, SECOND_HEX_NUM) + \
    HexOperation(FIRST_HEX_NUM, SECOND_HEX_NUM)
RESULT_MUL = HexOperation(FIRST_HEX_NUM, SECOND_HEX_NUM) * \
    HexOperation(FIRST_HEX_NUM, SECOND_HEX_NUM)
print(f'Сумма = {RESULT_SUM}, а произведение = {RESULT_MUL}')
