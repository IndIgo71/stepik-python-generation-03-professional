import re


regex = r'^\d{1,2}[A-Za-z]{3,}\.{,3}$'

print(bool(re.match(regex, '12___O.')))