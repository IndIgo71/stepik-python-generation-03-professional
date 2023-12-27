import json

with (open(file='data1.json', mode='r', encoding='utf-8') as file1,
      open(file='data2.json', mode='r', encoding='utf-8') as file2,
      open(file='data_merge.json', mode='w', encoding='utf-8') as outfile):
    data1 = json.load(file1)
    data2 = json.load(file2)
    data1.update(data2)

    json.dump(data1, outfile, ensure_ascii=False, indent=3)
