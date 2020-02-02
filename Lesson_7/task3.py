"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint, choice
from statistics import median


def quick_sort(lst):
    """
    Функция сортировки.
    """
    if len(lst) <= 1:
        return lst
    else:
        random_item = choice(lst)
        left = []
        middle = []
        right = []
        for elem in lst:
            if elem < random_item:
                left.append(elem)
            elif elem > random_item:
                right.append(elem)
            else:
                middle.append(elem)
        return quick_sort(left) + middle + quick_sort(right)


USER_M = int(input('Введите число для расчета размера массива: '))
TEST_LST = [randint(-100, 100) for _ in range(2*USER_M + 1)]
SORTED_ARRAY = quick_sort(TEST_LST)  # Сортируем массив
print(f'Сгенерированный массив: {TEST_LST}')
print(f'Значение Медианы (модуль статистики): {median(TEST_LST)}')
print(f'Значение Медианы (методом сортировки): {SORTED_ARRAY[USER_M]}')
