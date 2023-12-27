from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

dates = [start + timedelta(days=i) for i in range((end - start).days + 1)]

start = min(dt for dt in dates if (dt.day + dt.month) % 2 != 0)
dates = dates[dates.index(start):]

for dt in dates[::3]:
    if dt.weekday() not in (0, 3):
        print(dt.strftime(pattern))
