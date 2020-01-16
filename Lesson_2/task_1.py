"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
import sys


def inputs():
    """Функция пользовательского ввода."""
    while 1 != 0:
        try:
            first, second = input(
                'Введите два числа через пробел: ').split(' ')
            break
        except ValueError:
            print('Попробуйте ещё раз')
    operation = input(
        'Введите знак операции (+,-,*,/),\nДля выхода введите 0: ')
    return int(first), int(second), operation


USER_OPERATION = input(
    'Добро пожаловать в "калькулятор на минималках" \nНачнём? (y/n): ')
if USER_OPERATION in ('y', 'д'):
    while USER_OPERATION != 0:
        USER_A, USER_B, USER_OPERATION = inputs()
        if USER_OPERATION == '+':
            print(f'Сумма равна {USER_A + USER_B}.')
        elif USER_OPERATION == '-':
            print(f'Разница равна {USER_A - USER_B}.')
        elif USER_OPERATION == '*':
            print(f'Произведение равно {USER_A * USER_B}.')
        elif USER_OPERATION == '/':
            if USER_B == 0:
                print('Извините, на 0 делить нельзя!')
            else:
                print(f'Частное равно {round((USER_A / USER_B), 3)}.')
        elif USER_OPERATION == '0':
            print('Спасибо, что воспользовались программой! \nДо новых встреч')
            break
        else:
            print(
                'К сожалению, вы ввели некорректный знак операции. \nПопробуйте снова ->')
elif USER_OPERATION in ('n', 'н'):
    print('Спасибо, до новых встреч!')
else:
    print('Извините, произошёл сбой.')


# Вариант через рекурссию
def calculator():
    """Калькулятор"""
    first = float(input('Введите число a: '))
    second = float(input('Введите число b: '))
    action = input('Введите действие: + - * / 0 - для выхода ')
    if action == '0':
        sys.exit()
    if action == '/' and second == 0:
        print('Извините, на 0 делить нельзя!')
        calculator()
    print(f'{first} {action} {second} = {eval(f"{first} {action} {second}")}')
    calculator()


calculator()
