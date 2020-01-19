"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def count_multiplicity(start_divider, end_divider, start_dividend, end_dividend):
    """Функция подсчёта кратности чисел двух диапазонов"""
    first_range = [i for i in range(start_divider, (end_divider + 1))]
    second_range = [i for i in range(start_dividend, (end_dividend + 1))]
    for unit in first_range:
        counter = 0
        for i in second_range:
            if i % unit == 0:
                counter += 1
        print(f'В указанном диапазоне {counter} чисел кратны {unit}')


count_multiplicity(2, 9, 2, 99)
