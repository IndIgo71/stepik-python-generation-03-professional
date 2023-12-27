from datetime import date


def date_formatter(country_code):
    loc = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def inner(dt: date):
        return dt.strftime(loc[country_code])

    return inner
