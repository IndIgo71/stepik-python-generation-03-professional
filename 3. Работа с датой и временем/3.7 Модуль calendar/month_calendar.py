import calendar

year, month = input().split()
print(calendar.month(int(year), list(calendar.month_abbr).index(month)))
