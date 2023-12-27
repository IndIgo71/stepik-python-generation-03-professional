import re

regex = r'[A-Z]{1,2}\d[\dA-Z]? \d[ABD-HJLNP-UW-Z]{2}'

print(re.findall(regex,'Our postcodes. Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS'))
print(re.findall(regex, 'PR0V 3RUA6. 0GHZ9a 9UY'))
print(re.findall(regex, 'PR1V 0EC TI1M 1IY TI1M 1KO PR1М 0Е PR1V 0MV'))