"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
# Вариант №1
EVEN = 0
ODD = 0


def even_odd(num):
    """Функция проверки на чётность"""
    if int(num) % 2 == 0:
        global EVEN
        EVEN += 1
    else:
        global ODD
        ODD += 1


print('Добро пожаловать в счётчик цифр \nУзнаем, сколько чётных и нечётных в вашем чмсле')
while 1 > 0:
    user_num = input('Введите 4-х значное натуральное число: ')
    user_num = ' '.join(user_num)
    try:
        user_a, user_b, user_c, user_d = user_num.split(' ')
        break
    except ValueError:
        print('Введено некорректное число. \nПовторите попытку.')

even_odd(user_a)
even_odd(user_b)
even_odd(user_c)
even_odd(user_d)
print(f'{EVEN} чётных и {ODD} нечётных цифр в числе')

# Вариант №2
