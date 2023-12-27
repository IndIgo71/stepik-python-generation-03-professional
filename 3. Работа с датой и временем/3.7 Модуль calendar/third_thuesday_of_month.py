import calendar
from datetime import date

year = int(input())
happy_days = []
for month in range(1, 13):
    weeks = calendar.monthcalendar(year, month)
    happy_week_idx = 3 if weeks[0][3] == 0 else 2
    happy_days.append(date(year, month, weeks[happy_week_idx][3]))
print(*map(lambda d: d.strftime('%d.%m.%Y'), sorted(happy_days)), sep='\n')
