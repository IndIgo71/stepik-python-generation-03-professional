def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return (res, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')

    return wrapper
