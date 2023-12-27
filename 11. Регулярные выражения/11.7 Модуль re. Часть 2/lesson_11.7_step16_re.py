import re
import sys

pattern = r'<a href=\"(.*)\">(.*)</a>'
text = sys.stdin.read()
for href, title in re.findall(pattern, text):
    print(f'{href}, {title}')
