from datetime import datetime

pattern = '%d.%m.%Y'
dates = list(map(lambda s: datetime.strptime(s, pattern), input().split()))

print([abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))])
