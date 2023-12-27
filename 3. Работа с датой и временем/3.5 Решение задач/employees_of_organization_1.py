from datetime import datetime

pattern = '%d.%m.%Y'

employees = {}
for _ in range(int(input())):
    *name, birthdate = input().split()
    birthdate = datetime.strptime(birthdate, pattern)
    employees.setdefault(birthdate, []).append(' '.join(name))

min_birthdate = min(employees)

if len(employees[min_birthdate]) > 1:
    print(f'{min_birthdate.strftime(pattern)} {len(employees[min_birthdate])}')
else:
    print(f'{min_birthdate.strftime(pattern)} {employees[min_birthdate][0]}')
