import re
import sys

pattern = r'<(\w*)(\s(\w*)=\")?'
text = sys.stdin.read()

res = dict()
for bracket in filter(None, re.findall(r'<(.+?)>', text)):
    for tag in re.findall(r'^(\w+)', bracket):
        res.setdefault(tag, set())
        for attr in re.findall(r'([^\"\s]*)=', bracket):
            res[tag].add(attr)

for key, value in sorted(res.items()):
    print(f'{key}: {", ".join(sorted(value))}')
