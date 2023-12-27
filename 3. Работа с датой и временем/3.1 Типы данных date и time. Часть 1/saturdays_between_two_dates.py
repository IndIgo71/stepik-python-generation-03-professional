from datetime import date


def saturdays_between_two_dates(start: date, end: date):
    if start > end:
        start, end = end, start
    return len(
        list(filter(lambda x: date.fromordinal(x).weekday() == 5, range(start.toordinal(), end.toordinal() + 1))))
