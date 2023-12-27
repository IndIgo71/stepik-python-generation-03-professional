from datetime import datetime


def str_to_frmt_dtm(str):
    return datetime.strptime(str, '%d.%m.%Y')


def get_range_dates(rng) -> list:
    start, end = rng.split('-')
    start, end = str_to_frmt_dtm(start), str_to_frmt_dtm(end)
    end = end.replace(day=end.day + 1)
    return list(range(start.toordinal(), end.toordinal()))


def is_available_date(booked_dates, date_for_booking) -> bool:
    bdts = []
    for booked_date in booked_dates:
        if '-' in booked_date:
            bdts.extend(get_range_dates(booked_date))
        else:
            bdts.append(str_to_frmt_dtm(booked_date).toordinal())
    bdts = set(bdts)

    if '-' in date_for_booking:
        date_for_booking = set(get_range_dates(date_for_booking))
    else:
        date_for_booking = {str_to_frmt_dtm(date_for_booking).toordinal(), }

    return bdts.isdisjoint(date_for_booking)
