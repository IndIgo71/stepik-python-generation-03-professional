from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
print(dt.strftime(pattern))
for i in range(1, 10):
    dt += timedelta(days=i + 1)
    print(dt.strftime(pattern))
