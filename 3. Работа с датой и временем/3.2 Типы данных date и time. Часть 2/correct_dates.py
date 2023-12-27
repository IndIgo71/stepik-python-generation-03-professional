from datetime import date


def is_correct(day, month, year):
    try:
        dt = date(year, month, day)
        return True
    except ValueError:
        return False


result = []
total = 0
while True:
    t = input()
    if t == 'end':
        break
    day, month, year = t.split('.')
    if is_correct(int(day), int(month), int(year)):
        total += 1
        result.append('Корректная')
    else:
        result.append('Некорректная')

print(*result, sep='\n')
print(total)
