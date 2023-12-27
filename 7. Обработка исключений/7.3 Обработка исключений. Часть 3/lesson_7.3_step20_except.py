import calendar

try:
    n = int(input())
    if 1 <= n <= 12:
        print(calendar.month_name[n])
    else:
        print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
