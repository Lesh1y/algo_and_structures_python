"""4.	Определить, какое число в массиве встречается чаще всего."""

TEST_LST = [0, 1, 2, 3, 4, 5, 6, 7, 0]
ELEMENT = 0
COUNT_ELEM = 0
for elem in TEST_LST:
    if TEST_LST.count(elem) > COUNT_ELEM:
        ELEMENT = elem
        COUNT_ELEM = TEST_LST.count(elem)
if COUNT_ELEM <= 1:
    print('В массиве нет повторяющихся элементов')
else:
    print(f'Число {ELEMENT} встречается {COUNT_ELEM} раз')
