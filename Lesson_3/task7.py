"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint


def generate_lst(n):
    """Функция генерирует список случайных чисел"""
    lst = []
    while n > 0:
        lst.append(randint(0, 100))
        n -= 1
    return lst


USER_LST = generate_lst(
    int(input('Введите кол-во случайных элементов массива: ')))
TEST_LST = sorted(USER_LST.copy())
MIN1 = TEST_LST[0]
MIN2 = TEST_LST[1]
print(USER_LST)
print(MIN1, MIN2)
