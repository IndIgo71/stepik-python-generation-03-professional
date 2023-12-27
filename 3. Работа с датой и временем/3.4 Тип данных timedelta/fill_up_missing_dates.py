from datetime import datetime, timedelta


def fill_up_missing_dates(dates, pattern='%d.%m.%Y'):
    dates = list(map(lambda s: datetime.strptime(s, pattern), dates))
    result = dates.copy()
    for i in range((max(dates) - min(dates)).days + 1):
        dt = min(dates) + timedelta(days=i)
        if dt not in dates:
            result.append(min(dates) + timedelta(days=i))

    return list(map(lambda dt: dt.strftime(pattern), sorted(result)))
