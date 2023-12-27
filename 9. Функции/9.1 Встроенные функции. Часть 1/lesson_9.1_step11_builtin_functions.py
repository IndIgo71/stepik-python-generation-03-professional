def custom_isinstance(objests, typeinfo):
    return len(list(filter(lambda obj: isinstance(obj, typeinfo), objests)))
