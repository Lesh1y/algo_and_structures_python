"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

USER_NUMBER = int(input('Введите трёхзначное число: '))
# тут, по-хорошему, нужен while, но мы верим в пользователя и считаем, что
# он ошибётся всего раз в каждую сторону
if USER_NUMBER <= 99:
    print('Ваше число имеет меньше трёх знаков!')
    USER_NUMBER = int(input('Введите трёхзначное число: '))
    if USER_NUMBER <= 99:
        print('Ваше число имеет меньше трёх знаков! Попробуйте снова.')
    elif USER_NUMBER >= 1000:
        print('Ваше число имеет больше трёх знаков! Попробуйте снова.')
    else:
        SUM_USER_NUMBER = USER_NUMBER // 100 + \
            USER_NUMBER % 10 + (USER_NUMBER // 10) % 10
        PRODUCT_USER_NUMBER = (USER_NUMBER // 100) * \
            (USER_NUMBER % 10) * ((USER_NUMBER // 10) % 10)
        print(
            f'Сумма цифр вашего числа равна {SUM_USER_NUMBER}, а произведение - {PRODUCT_USER_NUMBER}')
else:
    SUM_USER_NUMBER = USER_NUMBER // 100 + \
        USER_NUMBER % 10 + (USER_NUMBER // 10) % 10
    PRODUCT_USER_NUMBER = (USER_NUMBER // 100) * \
        (USER_NUMBER % 10) * ((USER_NUMBER // 10) % 10)
    print(
        f'Сумма цифр вашего числа равна {SUM_USER_NUMBER}, а произведение равно {PRODUCT_USER_NUMBER}')
