import re
import sys

pattern = r'^(\w+)\1$'
for login in map(str.strip, sys.stdin.readlines()):
    match = re.fullmatch(pattern, login)
    if match:
        print(match.group())
