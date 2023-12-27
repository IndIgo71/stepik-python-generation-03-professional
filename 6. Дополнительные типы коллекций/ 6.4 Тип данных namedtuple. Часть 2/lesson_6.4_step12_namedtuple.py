import csv
from collections import namedtuple
from datetime import datetime

with open('meetings.csv', 'r', encoding='utf-8', newline='') as file:
    content = csv.DictReader(file, delimiter=',')
    Meeting = namedtuple('Meeting', content.fieldnames)
    meetings = [Meeting(**m) for m in content]
    for meeting in sorted(meetings,
                          key=lambda x: datetime.strptime(f'{x.meeting_date} {x.meeting_time}', '%d.%m.%Y %H:%M')):
        print(f'{meeting.surname} {meeting.name}')
