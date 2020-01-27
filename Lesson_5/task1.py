"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
# Namedtuple из примера
from collections import nemedtuple

COUNT = int(input('Введите кол-во компаний: '))
COMPANIES = namedtuple('Company', ' name quarter_1 quarter_2 quarter_3 quarter_4')
PROFIT_AVER = {}

for i in range(COUNT):
    COMPANY = COMPANIES(name=input('Введите название компании: '),
                        quarter_1=int(input('Введите прибыль за первый квартал: ')),
                        quarter_2=int(input('Введите прибыль за второй квартал: ')),
                        quarter_3=int(input('Введите прибыль за третий квартал: ')),
                        quarter_4=int(input('Введите прибыль за четвёртый квартал: ')),)
    PROFIT_AVER[COMPANY.name] = (COMPANY.quarter_1 + COMPANY.quarter_2 + COMPANY.quarter_3 + COMPANY.quarter_4)

# print(COMPANIES)

TOTAL_AVER = 0
for value in PROFIT_AVER.values():
    TOTAL_AVER += value
TOTAL_AVER = TOTAL_AVER / COUNT

for key, value in PROFIT_AVER.items():
    if value > TOTAL_AVER:
        print(f'{key} - прибыль выше среднего')
    elif value < TOTAL_AVER:
        print(f'{key} - прибыль ниже среднего')
    elif value == TOTAL_AVER:
        print(f'{key} - средняя прибыль')
