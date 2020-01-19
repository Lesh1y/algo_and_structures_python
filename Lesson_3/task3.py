"""
3. В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""

from random import randint


def generate_lst(n):
    """Функция генерирует список случайных чисел"""
    lst = []
    while n > 0:
        lst.append(randint(0, 100))
        n -= 1
    return lst


def replace_min_max(lst):
    """Функция смены мест min и max"""
    min_number = lst[0]
    max_number = lst[0]
    min_index = 0
    max_index = 0
    for i, j in enumerate(lst[1:]):
        if j < min_number:
            min_number = j
            min_index = i + 1
        if j > max_number:
            max_number = j
            max_index = i + 1
    print(f'Ваш массив случайных чисел: {lst}')
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return print(
        f'Минимальное значение массива: {min_number}\nМаксимальное значение массива: {max_number}\n'
        f'Меняю значения местами...\nИтоговый вариант массива: {lst}')


print(f'Добро пожаловать!\nЯ могу поменять местами минимальный и максимальный элементы массива')
N = int(input('Введите длину массива случайных чисел: '))
replace_min_max(generate_lst(N))
