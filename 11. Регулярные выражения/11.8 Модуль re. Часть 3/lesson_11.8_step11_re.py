import keyword
import re


def get_keyword(match_obj: re.Match) -> str:
    s = match_obj.group(0)
    if s.lower() in map(str.lower, keyword.kwlist):
        return '<kw>'
    return s


if __name__ == '__main__':
    print(re.sub(r'\b\w+\b', get_keyword, input(), flags=re.I))
