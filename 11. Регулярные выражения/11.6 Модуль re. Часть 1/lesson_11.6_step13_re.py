import re
import sys

pattern = r'(^beegeek.*beegeek$)?(^beegeek.*|.*beegeek$)?(.*beegeek.*)?'
total = 0
for line in map(str.strip, sys.stdin.readlines()):
    match = re.search(pattern, line)
    total += max([3 - i for i, v in enumerate(match.groups()) if v], default=0)

print(total)
