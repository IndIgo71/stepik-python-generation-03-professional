import json

with (open(file='data.json', mode='r', encoding='utf-8') as file,
      open(file='updated_data.json', mode='w', encoding='utf-8') as outfile):
    data = json.load(file)
    result = []
    for item in data:
        if isinstance(item, bool):
            result.append(not item)
        elif isinstance(item, str):
            result.append(item + '!')
        elif isinstance(item, int):
            result.append(item + 1)
        elif isinstance(item, list):
            result.append(item * 2)
        elif isinstance(item, dict):
            item['newkey'] = None
            result.append(item)
        elif item is None:
            continue

    json.dump(result, outfile, ensure_ascii=False, indent=3)
