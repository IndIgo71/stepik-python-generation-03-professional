import calendar

year, month_name = input().split()
month = list(calendar.month_name).index(month_name)

print(calendar.monthrange(int(year), month)[1])
