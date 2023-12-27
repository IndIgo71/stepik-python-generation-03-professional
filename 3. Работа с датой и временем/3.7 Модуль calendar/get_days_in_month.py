from datetime import date
import calendar


def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    return sorted([date(year, month, i + 1) for i in range(calendar.monthrange(year, month)[1])])


print(get_days_in_month(1982, 'January'))