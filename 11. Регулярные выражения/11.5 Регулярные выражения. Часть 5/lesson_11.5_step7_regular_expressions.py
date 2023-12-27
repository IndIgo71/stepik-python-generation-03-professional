import re


regex = r'\d{5}(-\d{4})?'

print(re.findall(regex, 'My old poscode: 18491 And new: 48034-1234'))