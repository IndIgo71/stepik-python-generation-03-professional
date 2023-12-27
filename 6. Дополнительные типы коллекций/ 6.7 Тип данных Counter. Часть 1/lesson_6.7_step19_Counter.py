from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    text = file.read()
    alphabet = Counter(filter(lambda x: x.isalpha(), text.lower()))
    for k, v in sorted(alphabet.items()):
        print(f'{k}: {v}')
