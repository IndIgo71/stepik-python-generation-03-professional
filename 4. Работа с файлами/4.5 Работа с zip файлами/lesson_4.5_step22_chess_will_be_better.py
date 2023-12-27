"""
Обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены
в лексикографическом порядке имен, а при совпадении — в лексикографическом
порядке фамилий, каждый на отдельной строке.

https://stepik.org/lesson/547172/step/22?unit=540798
"""

import json
from zipfile import ZipFile

players = []
with ZipFile('data.zip') as zip_file:
    files = [file for file in zip_file.infolist() if not file.is_dir() and file.filename.endswith('.json')]
    for file in files:
        zip_file.extract(file.filename)
        with open(file.filename, mode='r', encoding='utf-8') as json_file:
            try:
                content = json.load(json_file)
                if content['team'] == 'Arsenal':
                    players.append((content['first_name'], content['last_name']))
            except:
                continue

print(*map(lambda p: f'{p[0]} {p[1]}', sorted(players)), sep='\n')
