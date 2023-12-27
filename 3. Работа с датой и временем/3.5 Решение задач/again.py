from datetime import datetime, timedelta

schedule = {
    'Mon': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Tue': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Wed': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Thu': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Fri': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Sat': {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    'Sun': {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
}

dtm = datetime.strptime(input(), '%d.%m.%Y %H:%M')
day_schedule = schedule[dtm.strftime('%a')]
dtm_today = timedelta(hours=dtm.hour, minutes=dtm.minute)

if dtm_today >= day_schedule['end'] or dtm_today < day_schedule['start']:
    print('Магазин не работает')
else:
    print(int((day_schedule['end'] - dtm_today).seconds / 60))
