import re

regex = r'<!--.*?-->'
print(re.findall(regex, '<!-- header of page --> <-- incorrect header of page !-->'))