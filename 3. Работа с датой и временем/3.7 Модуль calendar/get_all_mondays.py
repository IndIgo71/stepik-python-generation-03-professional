import calendar
from datetime import date


def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            if week[0]:
                mondays.append(date(year, month, week[0]))
    return sorted(mondays)
