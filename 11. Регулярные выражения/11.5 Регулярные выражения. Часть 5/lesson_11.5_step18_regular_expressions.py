import sys
import re

pattern = r'(?P<country_code>\d{1,3})([ -])(?P<city_code>\d{1,3})\2(?P<number>\d{4,10})'
for phone in map(str.strip, sys.stdin.readlines()):
    match = re.fullmatch(pattern, phone)
    if match:
        country, city, number = match.group('country_code', 'city_code', 'number')
        print(
            f'Код страны: {country}, Код города: {city}, Номер: {number}')
