from datetime import date


def get_min_max(dates):
    if not dates:
        return tuple()
    return min(dates), max(dates)
