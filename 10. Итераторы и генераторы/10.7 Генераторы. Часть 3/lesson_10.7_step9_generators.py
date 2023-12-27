from calendar import monthrange
from datetime import date


def years_days(year):
    for month in range(1, 13):
        for day in range(1, monthrange(year, month)[1] + 1):
            yield date(year, month, day)
