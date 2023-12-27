import sys
from datetime import datetime

dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
l = len(dates)
if all(map(lambda i: dates[i] < dates[i + 1], range(l - 1))):
    sys.stdout.write('ASC')
elif all(map(lambda i: dates[i] > dates[i + 1], range(l - 1))):
    sys.stdout.write('DESC')
else:
    sys.stdout.write('MIX')
