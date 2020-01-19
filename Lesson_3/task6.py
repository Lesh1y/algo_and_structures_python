"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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
    int(input('Введите кол-во случайных элементов списка: ')))
MAX_NUM_INDEX = 0
MIN_NUM_INDEX = 0

for i in range(len(USER_LST)):
    if USER_LST[i] > USER_LST[MAX_NUM_INDEX]:
        MAX_NUM_INDEX = i
    if USER_LST[i] < USER_LST[MIN_NUM_INDEX]:
        MIN_NUM_INDEX = i
GAP = 0
if MIN_NUM_INDEX < MAX_NUM_INDEX:
    GAP = USER_LST[min(MAX_NUM_INDEX, MIN_NUM_INDEX) +
                   1:max(MAX_NUM_INDEX, MIN_NUM_INDEX)]
else:
    GAP = USER_LST[min(MIN_NUM_INDEX, MAX_NUM_INDEX) +
                   1:max(MIN_NUM_INDEX, MAX_NUM_INDEX)]
print(USER_LST)
print(f'Максимальный элемент массива = {USER_LST[MAX_NUM_INDEX]},'
      f' а минимальный = {USER_LST[MIN_NUM_INDEX]}')
print(f'Между ними находятся следующие элементы: {GAP}')
SUM_GAP = 0
for i in GAP:
    SUM_GAP += i
print(f'Сумма этих элементов = {SUM_GAP}')
