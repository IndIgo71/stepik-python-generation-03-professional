import json
from datetime import datetime

with open('pools.json', 'r', encoding='utf-8') as infile:
    pools = json.load(infile)
    res = []
    time_pattern = '%H:%M'
    for pool in pools:
        if 'Понедельник' in pool['WorkingHoursSummer']:
            start, end = map(lambda d: datetime.strptime(d, time_pattern),
                             pool['WorkingHoursSummer']['Понедельник'].split('-'))
            if start <= datetime.strptime('10:00', time_pattern) and end >= datetime.strptime('12:00', time_pattern):
                res.append((pool['DimensionsSummer']['Length'], pool['DimensionsSummer']['Width'], pool['Address']))

    n = max(res, key=lambda x: (x[0], x[1]))
    print(f'{n[0]}x{n[1]}')
    print(n[2])
