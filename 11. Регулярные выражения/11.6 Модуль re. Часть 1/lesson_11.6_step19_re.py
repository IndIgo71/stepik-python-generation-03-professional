import re

pattern = r'Здравствуйте|Доброе утро|Добрый день|Добрый вечер'
text = input()
print(bool(re.match(pattern, text, re.I)))
