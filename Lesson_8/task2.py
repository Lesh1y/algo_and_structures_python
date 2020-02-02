"""
2. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

USER_STR = input('ведите строку из маленьких латинских букв: ')
RESULT = set()

N = len(USER_STR)
for i in range(N):
    if i == 0:
        N = len(USER_STR) - 1
    else:
        N = len(USER_STR)
    for j in range(N, i, -1):
        RESULT.add(hashlib.sha1(USER_STR[i:j].encode('utf-8')).hexdigest())
print(
    f'Количество различных подстрок в строке "{USER_STR}" равнро {len(RESULT)}!')
