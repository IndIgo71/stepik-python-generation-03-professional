import re


regex = r'(([0-9]{3})|(\([0-9]{3}\)))[- ]\d{3}[- ]\d{4}'

print(re.match(regex, 'Badeline: (810)-555-1234'))