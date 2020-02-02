"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint
import timeit

USER_LEN = int(input('Введите длинну массива: '))
USER_LIST = [randint(-100, 100) for _ in range(USER_LEN)]
print(f'Оригинальный список: \n{USER_LIST}')


def bubble_sort(lst, lens):
    """
    Функция сортирует по убыванию методом "пузырька"
    """
    for i in range(lens):
        for j in range(lens - i):
            if lst[j] < lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]

    return lst


def bubble_sort_2(lst, lens):
    """
    Доработаная функция сортировки пузырька,
    в ситуации когда нечего изменять в массиве функция завершается досрочно
    """
    for i in range(lens):
        mod = False
        for j in range(lens - i):
            if lst[j] < lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                mod = True
        if not mod:
            return lst
    return lst


print('Время выполнения обычной сортировки пузырьком:')
print(timeit.timeit('bubble_sort(USER_LIST, USER_LEN-1)',
                    setup='from __main__ import bubble_sort, USER_LIST, USER_LEN', number=1000))
print('Время выполнения модифицированной сортировки пузырьком:')
print(timeit.timeit('bubble_sort_2(USER_LIST, USER_LEN-1)',
                    setup='from __main__ import bubble_sort_2, USER_LIST, USER_LEN', number=1000))

print(f'Отсортированый список: \n{USER_LIST}')
