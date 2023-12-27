from datetime import date


def is_correct(day, month, year):
    try:
        dt = date(year, month, day)
        return True
    except ValueError:
        return False
