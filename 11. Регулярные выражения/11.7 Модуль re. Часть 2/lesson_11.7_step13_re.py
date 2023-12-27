import re

word, text = input(), input()
print(len(re.findall(rf'\b{word[:-2]}[sz]e\b', text, flags=re.I)))
