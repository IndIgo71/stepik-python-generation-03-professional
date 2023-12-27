import re


def normalize_jpeg(filename):
    return re.sub(r'\.(jpeg|jpg)$', '.jpg', filename, flags=re.I)
