"""
9. Вводятся три разных числа. Найти, какое из них
является средним (больше одного, но меньше другого).
"""

print('Найдём среднее число')
A, B, C = input('Введите три числа через пробел: ').split(' ')
middle = int(A)
if middle > int(B) and middle > int(C):
    middle = int(B)
    if middle < int(A) and middle < int(C):
        middle = int(C)
        print(f'\tСреднее из них {middle}')
    else:
        print(f'\tСреднее из них {middle}')
else:
    print(f'\tСреднее из них {middle}')
