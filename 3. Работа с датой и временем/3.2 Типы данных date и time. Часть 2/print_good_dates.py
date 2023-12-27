from datetime import date


def print_good_dates(dates):
    year = 1992
    age = 29
    good_dates = sorted([dt for dt in sorted(dates) if dt.year == year and dt.month + dt.day == age])
    if good_dates:
        for dt in good_dates:
            print(dt.strftime('%B %d, %Y'))
