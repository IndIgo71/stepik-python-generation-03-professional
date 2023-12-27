import csv
import json

with (open(file='playgrounds.csv', mode='r', encoding='utf-8') as infile,
      open(file='addresses.json', mode='w', encoding='utf-8') as outfile):
    reader = csv.DictReader(infile, delimiter=';')
    adresses = dict()
    for row in reader:
        adresses.setdefault(row['AdmArea'], dict()).setdefault(row['District'], list()).append(row['Address'])

    json.dump(adresses, outfile, ensure_ascii=False, indent=3)
