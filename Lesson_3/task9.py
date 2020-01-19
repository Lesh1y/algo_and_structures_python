"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import random

MATRIX = []
for i in range(4):
    MATRIX.append([])
    for j in range(4):
        MATRIX[i].append(random.randint(1, 100))

Y = []
X = []
for i in range(len(MATRIX)):
    Y.append([])
    for j in range(len(MATRIX)):
        Y[i].append(MATRIX[j][i])
    X.append(min(Y[i]))

for i in MATRIX:
    print(i)
print(max(X))
