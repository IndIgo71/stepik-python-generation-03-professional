from datetime import date

day = 13
min_month = 1
max_month = 12
min_year = 1
max_year = 9999
count_days = {}
for year in range(min_year, max_year + 1):
    for month in range(min_month, max_month + 1):
        friday = date(year, month, day).strftime("%u")
        count_days[friday] = count_days.get(friday, 0) + 1
print(*[count_days[k] for k in sorted(count_days.keys())], sep="\n")
