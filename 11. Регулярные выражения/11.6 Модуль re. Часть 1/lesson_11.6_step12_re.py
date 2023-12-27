import re
import sys

pattern_bee = r'(bee).*\1'
pattern_geek = r'\bgeek\b'
b, g = 0, 0
for line in map(str.strip, sys.stdin.readlines()):
    b += bool(re.search(pattern_bee, line))
    g += bool(re.search(pattern_geek, line))

print(b, g, sep='\n')
