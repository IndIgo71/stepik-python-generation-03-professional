import re


def multiply_str(match_obj: re.Match) -> str:
    return match_obj.group(2) * int(match_obj.group(1))


if __name__ == '__main__':
    text = input()
    while '(' in text:
        text = re.sub(r'(\d+)\((\w+)\)', multiply_str, text)
    print(text)
