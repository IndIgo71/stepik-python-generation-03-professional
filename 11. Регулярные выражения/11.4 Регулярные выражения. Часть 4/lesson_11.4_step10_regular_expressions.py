import re

regex = r'\bA\b|\bAn\b|\ban\b|\ba\b'

print(re.findall(regex,'A cow is an animal.'))
print(re.findall(regex, 'I have been reading this text for aN hour. Сan you give me this book? AN or an apple'))
print(re.findall(regex, 'An acle, a Ancle, A antarktida, an Any'))