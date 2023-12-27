from datetime import datetime
import calendar

dt = datetime.strptime(input(), '%Y-%m-%d')
print(calendar.day_name[dt.weekday()])
