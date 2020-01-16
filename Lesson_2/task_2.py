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
while True:
    USER_NUM = input('Введите 4-х значное натуральное число: ')
    USER_NUM = ' '.join(USER_NUM)
    try:
        USER_A, USER_B, USER_C, USER_D = USER_NUM.split(' ')
        break
    except ValueError:
        print('Введено некорректное число. \nПовторите попытку.')

even_odd(USER_A)
even_odd(USER_B)
even_odd(USER_C)
even_odd(USER_D)
print(f'{EVEN} чётных и {ODD} нечётных цифр в числе')


# Вариант №2
def calc_even(user_number):
    """ функция рассчитывает количество четных цифр введённого числа"""

    return len(str(user_number)) - calc_odd(user_number)


def calc_odd(user_number):
    """ функция вычисляет количество нечетных цифр введённого числа"""

    if len(str(user_number)) == 1:
        if (user_number % 2) == 0:
            return 0
        return 1
    i = user_number // (10 ** (len(str(user_number)) - 1))
    qty = 1 if (i % 2) else 0  # предварительное количество
    return calc_odd(user_number - i *
                    (10 ** (len(str(user_number)) - 1))) + qty


while True:
    try:
        USER_NUMBER = int(input('Ведите натуральное число: '))
        if USER_NUMBER <= 0:
            print('Введите корректное натуральное число.')
            continue
        print(
            f'Количество чётных цифр в числе {USER_NUMBER}: {calc_even(USER_NUMBER)}')
        print(
            f'Количество нечётных цифр в числе {USER_NUMBER}: {calc_odd(USER_NUMBER)}')
        break
    except ValueError:
        print('Ведите натуральное число.')
