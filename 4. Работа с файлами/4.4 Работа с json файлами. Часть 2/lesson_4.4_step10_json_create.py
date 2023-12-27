import json

with (open(file='countries.json', mode='r', encoding='utf-8') as country_file,
      open(file='religion.json', mode='w', encoding='utf-8') as religion_file):
    content = json.load(country_file)
    religions = dict()
    for data in content:
        religions.setdefault(data['religion'], []).append(data['country'])

    json.dump(religions, religion_file, ensure_ascii=False, indent=3)
