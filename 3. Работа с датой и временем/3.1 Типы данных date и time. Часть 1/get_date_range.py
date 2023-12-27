from datetime import date


def get_date_range(start: date, end: date):
    if start > end:
        return []
    else:
        return [date.fromordinal(start.toordinal() + i) for i in range(end.toordinal() - start.toordinal() + 1)]
