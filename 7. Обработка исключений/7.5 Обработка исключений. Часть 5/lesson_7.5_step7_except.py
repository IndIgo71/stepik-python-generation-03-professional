import re


def is_good_password(string):
    pattern = r'^(?=.*\d)(?=.*[a-zа-я])(?=.*[A-ZА-Я]).{9,}$'
    if re.match(pattern, string):
        return True
    else:
        return False
