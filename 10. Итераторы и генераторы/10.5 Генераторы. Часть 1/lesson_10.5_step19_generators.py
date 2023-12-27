from datetime import date, timedelta


def dates(start: date, count: int = None):
    if not count:
        count = (date.max - start).days + 1
    yield from (start + timedelta(days=i) for i in range(count))
