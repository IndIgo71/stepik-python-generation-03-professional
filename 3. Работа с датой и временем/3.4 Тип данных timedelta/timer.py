from datetime import datetime, timedelta

pattern = '%H:%M:%S'
dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))

print(dt.strftime(pattern))
