def sourcetemplate(url):
    def inner(**kwargs):
        if kwargs:
            return f'{url}?{"&".join(f"{k}={v}" for k, v in sorted(kwargs.items()))}'
        return url

    return inner
