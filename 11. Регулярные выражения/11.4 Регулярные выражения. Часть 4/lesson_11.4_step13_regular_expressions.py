import re


regex = r'^\d{2,}[a-z]*[A-Z]*$'

print(bool(re.match(regex, '51tePIK   ')))