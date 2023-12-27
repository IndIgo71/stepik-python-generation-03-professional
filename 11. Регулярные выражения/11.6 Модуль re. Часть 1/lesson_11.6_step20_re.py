import re
import sys

total = 0
for line in map(str.strip, sys.stdin.readlines()):
    total += bool(re.search(r'beegeek', line, re.I | re.M))
print(total)
