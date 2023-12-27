import re

a, b = map(int, input().split())
text = input()
regex = re.compile(r'\W*(\d+)\W*')
print(sum(map(int, regex.findall(text, pos=a, endpos=b))))
