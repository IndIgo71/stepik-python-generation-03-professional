from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits


def verification(login, password, success, failure):
    error_messages = {
        0: 'в пароле нет ни одной буквы',
        1: 'в пароле нет ни одной заглавной буквы',
        2: 'в пароле нет ни одной строчной буквы',
        3: 'в пароле нет ни одной цифры'
    }
    pwd = set(password)
    try:
        if not any(map(lambda x: x in ascii_letters, pwd)):
            err = 0
            raise
        if not any(map(lambda x: x in ascii_uppercase, pwd)):
            err = 1
            raise
        if not any(map(lambda x: x in ascii_lowercase, pwd)):
            err = 2
            raise
        if not any(map(lambda x: x in digits, pwd)):
            err = 3
            raise
    except Exception:
        failure(login, error_messages[err])
    else:
        success(login)
