from datetime import datetime

pattern = '%d.%m.%Y'
employees = {}
for _ in range(int(input())):
    *name, birthdate = input().split()
    birthdate = datetime.strptime(birthdate, pattern)
    employees.setdefault(birthdate, []).append(' '.join(name))

birthdate_quantity = {k: len(v) for k, v in employees.items()}
dates = list(
    map(lambda k: k, filter(lambda k: birthdate_quantity[k] == max(birthdate_quantity.values()), birthdate_quantity)))
print(*map(lambda d: d.strftime(pattern), sorted(dates)), sep='\n')
