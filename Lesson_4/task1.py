"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import Timer


def first_test():
    """Первый вариант"""
    user_num = int(''.join(str(e) for e in [i for i in range(100)]))
    m = 0
    while user_num > 0:
        m = m * 10 + user_num % 10
        user_num = user_num // 10
#    print(M)


def second_test():
    """Второй вариант"""
    user_num2 = ''.join(str(e) for e in [i for i in range(100)])
    m = [i for i in user_num2]
    result = ''.join(reversed(m))
#    print(result)


TEST1 = Timer('first_test()', 'from __main__ import first_test')
print('concat', TEST1.timeit(number=10000), 'milliseconds')
TEST2 = Timer('second_test()', 'from __main__ import second_test')
print('concat', TEST2.timeit(number=10000), 'milliseconds')


"""
Более лаконичный вариант №2. Сложность, как мне кажется,
1.квадратичная 2.линейная. При более высокой длине числа,
входящего в алгоритмы, скорость второго значительно выше,
чем у первого.
"""
