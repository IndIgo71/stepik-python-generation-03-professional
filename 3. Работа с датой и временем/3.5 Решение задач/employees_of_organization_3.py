from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
start_dt = datetime.strptime(input(), pattern)
end_dt = start_dt + timedelta(days=7)

employees = {}
for _ in range(int(input())):
    *name, birthday = input().split()
    dt = datetime.strptime(birthday, pattern)
    employees[dt] = employees.setdefault(dt, " ".join(name))

result = []
for dt in employees.keys():
    true_now_year = start_dt < dt.replace(year=start_dt.year) <= end_dt
    true_next_year = start_dt < dt.replace(year=start_dt.year + 1) <= end_dt
    if true_now_year or true_next_year:
        result.append(dt)

if result:
    print(employees[max(result)])
else:
    print('Дни рождения не планируются')
