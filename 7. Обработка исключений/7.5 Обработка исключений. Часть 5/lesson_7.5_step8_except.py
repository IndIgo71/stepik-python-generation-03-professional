import re


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    # pattern = r'^(?=.*\d)(?=.*[a-zа-я])(?=.*[A-ZА-Я]).{9,}$'
    if len(string) < 9:
        raise LengthError

    if not re.match(r'(?=.*[a-zа-я])(?=.*[A-ZА-Я]).*', string):
        raise LetterError

    if not re.match(r'(?=.*\d).*', string):
        raise DigitError

    return True
