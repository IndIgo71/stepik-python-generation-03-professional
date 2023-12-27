import re

regex = r'\b[A-Z]+\b'

print(re.findall(regex,"Why isn’t my progress in the APP synchrONized with my progress in the WEB version?"))
print(re.findall(regex, "OOO 'BEEGEEK'"))
print(re.findall(regex, 'I will go to the shop aNd you stay At home'))