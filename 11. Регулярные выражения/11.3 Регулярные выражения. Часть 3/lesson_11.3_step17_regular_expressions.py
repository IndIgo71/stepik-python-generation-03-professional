import re

regex = r'([A-Z]{5}\d{4}[A-Z]{1})'
print(re.findall(regex, 'first number is ABCD EZZPA1234ZaPMQ0000O, check thusEZZPA1234ZAPMQ0000O,'))