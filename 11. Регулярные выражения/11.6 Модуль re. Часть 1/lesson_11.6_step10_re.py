import re
import sys

pattern = r'^_\d+[A-Za-z]*_?$'
for login in map(str.strip, sys.stdin.readlines()):
    print(bool(re.match(pattern, login)))
