import re


def minimize_str(match_obj: re.Match) -> str:
    return match_obj.group(1) + match_obj.group(2)


text = input()
n = 1
while n:
    text, n = re.subn(r'\b(\W*)(\w+)(\W*)\b\2\b', minimize_str, text)
print(text)
