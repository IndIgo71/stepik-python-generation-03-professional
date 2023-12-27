from calendar import day_name
import locale


def get_weekday(number):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

    return day_name[number - 1].title()
