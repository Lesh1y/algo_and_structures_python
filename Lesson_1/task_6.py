"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

print('Определяем позицию буквы в алфовите')
LETTER = ord(input('\tВведите вашу букву: '))
RESULT = LETTER - 97 + 1
print(F'Её позиция {RESULT}')