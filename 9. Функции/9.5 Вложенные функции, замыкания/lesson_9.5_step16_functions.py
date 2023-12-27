def power(degree):
    def inner(x):
        return x ** degree

    return inner
