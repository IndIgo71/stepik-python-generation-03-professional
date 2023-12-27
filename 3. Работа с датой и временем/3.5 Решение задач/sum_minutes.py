from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

n = int(sum((datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')).total_seconds() // 60 for start, end in data))
print(n)
