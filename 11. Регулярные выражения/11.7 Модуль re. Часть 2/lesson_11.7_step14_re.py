import re

word, text = input(), input()
print(len(re.findall(rf'\b{word[:-3]}ou?r\b', text, flags=re.I)))
