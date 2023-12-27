from datetime import datetime


def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    elif 2 <= amount % 10 <= 4 and not (11 <= amount % 100 <= 14):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'


plural_dict = {
    'day': ("день", "дня", "дней"),
    'hour': ("час", "часа", "часов"),
    'minute': ("минута", "минуты", "минут"),
}

release_date = datetime(year=2022, month=11, day=8, hour=12, minute=0)
current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if current_date >= release_date:
    print('Курс уже вышел!')
else:
    rest_delta = release_date - current_date
    rest_days = rest_delta.days
    rest_hours = rest_delta.seconds // 3600
    rest_minutes = rest_delta.seconds // 60 - rest_hours * 60

    rest_days_text = choose_plural(rest_days, plural_dict['day'])
    rest_hours_text = choose_plural(rest_hours, plural_dict['hour'])
    rest_minutes_text = choose_plural(rest_minutes, plural_dict['minute'])

    if rest_days == 0 and rest_hours == 0:
        print(f'До выхода курса осталось: {rest_minutes_text}')
    elif rest_days == 0 and rest_minutes == 0:
        print(f'До выхода курса осталось: {rest_hours_text}')
    elif rest_hours == 0:
        print(f'До выхода курса осталось: {rest_days_text}')
    elif rest_days == 0:
        print(f'До выхода курса осталось: {rest_hours_text} и {rest_minutes_text}')
    else:
        print(f'До выхода курса осталось: {rest_days_text} и {rest_hours_text}')
