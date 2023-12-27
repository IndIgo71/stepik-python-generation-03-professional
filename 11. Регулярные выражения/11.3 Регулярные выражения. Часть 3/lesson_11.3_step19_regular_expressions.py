import re

regex = r'[a-z]{,3}\d{2,8}[A-Z]{3,}'
print(re.findall(regex, '1. name Tobot id: 234AZXR, 2. name Alph id: a6578ALPH, 3. name Teta id: abra0909CADABRA 4. name Alph up id: A6578ALPH'))