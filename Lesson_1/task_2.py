"""
2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

A = 5
B = 6

print("%d & %d = %d (%s)" % (A, B, A & B, bin(A & B)))
print("%d | %d = %d (%s)" % (A, B, A | B, bin(A | B)))
print("%d ^ %d = %d (%s)" % (A, B, A ^ B, bin(A ^ B)))
print("%d << 2 = %d (%s)" % (B, B << 2, bin(B << 2)))
print("%d >> 2 = %d (%s)" % (B, B >> 2, bin(B >> 2)))
