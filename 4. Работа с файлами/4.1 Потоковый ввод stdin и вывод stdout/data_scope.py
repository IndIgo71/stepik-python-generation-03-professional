import sys
from datetime import datetime

dates = [datetime.strptime(dt.strip(), '%Y-%m-%d') for dt in sys.stdin.readlines()]
print((max(dates) - min(dates)).days)
