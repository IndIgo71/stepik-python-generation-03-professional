import json

with (open(file='people.json', mode='r', encoding='utf-8') as file,
      open(file='updated_people.json', mode='w', encoding='utf-8') as outfile):
    data = json.load(file)
    keys = set()
    for d in data:
        keys.update(d.keys())

    for d in data:
        for k in keys:
            if k not in d:
                d[k] = None

    json.dump(data, outfile, ensure_ascii=False, indent=3)
