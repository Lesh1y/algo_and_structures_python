"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple, deque, Counter

# Вариант с namedtuple
CompaniesCards = namedtuple('Company', 'name First Second Third Fourth')


def input_namedtuple():
    """Функция запрашивает данные для заполнения именного кортежа"""
    company_info = CompaniesCards(
        name=input('Введите название компании: '),
        First=int(input('Введите прибыль за первый квартал: ')),
        Second=int(input('Введите прибыль за второй квартал: ')),
        Third=int(input('Введите прибыль за третий квартал: ')),
        Fourth=int(input('Введите прибыль за четвертый квартал: ')))
    return company_info


def average_income(info, count):
    """Функция считае среднюю прибыль по всем компаниям"""
    total_income = 0
    for company in range(count):
        total_income += (info[company].First +
                         info[company].Second +
                         info[company].Third +
                         info[company].Fourth)
    return total_income / count


def company_income(company):
    """Общая прибыль у отдеьно взятой фирмы"""
    return company.First + company.Second + company.Third + company.Fourth


def above_average_company(info, avg_res, count):
    """Отсортировка по двум спискам, компании с доходом выше среднего и оставшиеся(ниже среднего)"""
    best = []
    residue = []
    for i in range(count):
        if company_income(info[i]) > avg_res:
            best.append(info[i].name)
        else:
            residue.append(info[i].name)
    return best, residue


COUNT = int(input('Введите количество компаний для расчетов: '))
INFO = [(input_namedtuple()) for i in range(COUNT)]
# print(INFO)
AVG_RES = average_income(INFO, COUNT)
print(f'Средняя прибыль {round(AVG_RES, 2)}/год')
BESTS, REST = above_average_company(INFO, AVG_RES, COUNT)
print(f'Прибыль выше среднего у компании(й) {BESTS}'
      f'\nПрибыль ниже среднего у компании(й) {REST}')

# Вариант с Counter
COUNT = int(input('Введите количество компаний для расчетов: '))
ENTERPRISES = Counter()

for i in range(COUNT):
    company_name = input('Наименование предприятия: ')
    year_prof = 0
    for j in range(1, 5):
        part_prof = int(
            input(f'Прибыль предприятия {company_name} за {j} квартал: '))
        year_prof += part_prof
    ENTERPRISES[company_name] = year_prof

AVERAGE_PROF = round(sum(ENTERPRISES.values()) / COUNT, 2)
HIGH_PROF = [(key, val)
             for key, val in ENTERPRISES.items() if val >= AVERAGE_PROF]
LOW_PROF = [(key, val)
            for key, val in ENTERPRISES.items() if val < AVERAGE_PROF]

print(f'\nСредняя прибыль: {AVERAGE_PROF}')

print('\nУ следующих предприятий прибыль выше средней или равна ей: ')
for i in HIGH_PROF:
    print(f'Предприятие "{i[0]}" с годовой прибылью {float(i[1])}')

if LOW_PROF:
    print('\nУ следующих предприятий прибыль ниже средней: ')
    for i in LOW_PROF:
        print(f'Предприятие "{i[0]}" с годовой прибылью {float(i[1])}')

# Вариант с deque
COUNT = int(input('Введите количество компаний для расчетов: '))
COMPANY_LST = []
for i in range(COUNT):
    new_company = dict(
        name=input(f'Введите название компании {i + 1}: '),
        qp=deque(),
        q_sum=0.0)
    for qn in range(1, 5):
        new_company['qp'].append(
            float(input(f'Введите прибыль компании {i + 1} за {qn} квартал: ')))
    new_company['q_sum'] = sum(new_company['qp'])
    COMPANY_LST.append(new_company)
    print('-' * 15)

AVERAGE = sum([i.get('q_sum', 0.0) for i in COMPANY_LST]) / COUNT
print(f'Предприятия с прибылью выше среднего (среднее = {AVERAGE}): ', ', '.join(
    [f'{i.get("name")} ({i.get("q_sum")})' for i in COMPANY_LST if i.get('q_sum', 0.0) > AVERAGE]))

print(f'Предприятия с прибылью ниже среднего (среднее = {AVERAGE}): ', ', '.join(
    [f'{i.get("name")} ({i.get("q_sum")})' for i in COMPANY_LST if i.get('q_sum', 0.0) < AVERAGE]))

# Ещё один вариант с Counter
COUNT = int(input('Введите количество компаний для расчетов: '))
COMPANY_DICT = dict()

for i in range(COUNT):
    name = input('Введите название компании: ')
    quarters_prof = input(
        'Введите через пробел прибыль за каждый квартал (всего 4): ')
    profit = quarters_prof.split(' ')
    COMPANY_DICT[name] = profit
    print()

COMPANIES = Counter(COMPANY_DICT)
COMPANY_COUNT = 0
TOTAL_SUM = 0
for i in COMPANIES:
    my_sum = 0
    for j in COMPANIES[i]:
        my_sum += int(j)
    COMPANIES[i] = my_sum
    TOTAL_SUM += my_sum
    COMPANY_COUNT += 1
AVG = TOTAL_SUM / COMPANY_COUNT

print(f'Средняя годовая прибыль всехпредприятий: {AVG}')
BESTS = []
RESTS = []
for i in COMPANIES:
    if int(COMPANIES[i]) >= AVG:
        BESTS.append(i)
    else:
        RESTS.append(i)
print(
    f'\n\nКомпании с прибылью выше либо равной средней: {" ".join([i for i in BESTS])}')
print(f'Предприятия с прибылью ниже средней: {" ".join([i for i in RESTS])}')
