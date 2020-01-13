"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

N = int(input('Введите номер элемента: '))
ELEMENT = 1
FINAL_SUM = 0
for i in range(N):
    FINAL_SUM += ELEMENT
    ELEMENT /= -2
print(FINAL_SUM)
