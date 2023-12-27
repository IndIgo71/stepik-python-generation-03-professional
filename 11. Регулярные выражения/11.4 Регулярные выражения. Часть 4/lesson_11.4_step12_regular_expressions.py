import re

regex = r'.*?\(.*\).*'

print(re.findall(regex,"(41 + 9) * 2 = ?"))
print(re.findall(regex, "A synthesizer (also spelled synthesiser) is an electronic musical instrument that generates audio signals."))
print(re.findall(regex, 'It was to be both a technical and surprisingly emotional challenge!))'))