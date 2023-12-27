import re
import sys

pattern = r'(\s*\"{3}.*?\"{3})|(\n? *#.*?$)'
print(re.sub(pattern, r'', sys.stdin.read(), flags=re.S | re.M))
