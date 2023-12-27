import re

text, word = input(), input()
print(len(re.findall(rf'\b{word}\b', text)))
