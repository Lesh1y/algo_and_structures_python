"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merge_sort(lst):
    """
    Функция сортировки.
    """
    if len(lst) > 1:
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        return lst


TEST_LST = [random.uniform(0, 50) for _ in range(50)]
print(TEST_LST)
print(merge_sort(TEST_LST))
