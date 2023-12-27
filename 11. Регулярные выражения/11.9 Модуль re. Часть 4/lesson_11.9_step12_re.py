import re


def multiple_split(string: str, delimiters: list[str]) -> list[str]:
    return re.split(r'\s*(?:' + '|'.join(map(re.escape, delimiters)) + r')\s*', string)
