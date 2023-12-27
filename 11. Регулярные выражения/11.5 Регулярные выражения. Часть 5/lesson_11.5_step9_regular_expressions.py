import re


regex = r'((beegeek)+)+'
print(re.findall(regex, 'Correct name is beegeekbeegeek'))