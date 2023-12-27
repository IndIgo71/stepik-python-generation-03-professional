from datetime import datetime


def num_of_sundays(year: int):
    return int(datetime(year=year, month=12, day=31).strftime("%U"))
