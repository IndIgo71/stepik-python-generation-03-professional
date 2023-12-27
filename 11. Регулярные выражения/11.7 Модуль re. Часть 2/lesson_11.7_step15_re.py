import re


def abbreviate(phrase: str) -> str:
    return ''.join(map(str.upper, re.findall(r'\b\w|[A-Z]', phrase)))
