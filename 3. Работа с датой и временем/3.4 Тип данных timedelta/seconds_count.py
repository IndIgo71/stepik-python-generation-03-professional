from datetime import datetime, timedelta

hours, minutes, seconds = map(int, input().split(':'))
print((timedelta(hours=hours, minutes=minutes, seconds=seconds) - timedelta(hours=0, minutes=0, seconds=0)).seconds)
