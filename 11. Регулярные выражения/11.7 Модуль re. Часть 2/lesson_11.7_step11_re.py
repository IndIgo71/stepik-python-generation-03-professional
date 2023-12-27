import re

text, word = input(), input()
print(len(re.findall(rf'\B{word}\B', text)))
