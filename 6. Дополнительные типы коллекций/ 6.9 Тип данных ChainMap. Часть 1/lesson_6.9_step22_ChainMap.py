from collections import ChainMap
import json

with open('zoo.json', 'r', encoding='utf-8') as f:
    context = json.load(f)

    zoo = ChainMap(*context)
    print(sum(zoo.values()))
