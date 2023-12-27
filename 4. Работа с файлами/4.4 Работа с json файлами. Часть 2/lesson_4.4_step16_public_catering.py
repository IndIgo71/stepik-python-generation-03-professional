import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    content = json.load(file)
    objects = {}
    for row in content:
        objects.setdefault(row['TypeObject'], []).append((row['Name'], int(row['SeatsCount'])))

    result = {k: max(v, key=lambda x: x[1]) for k, v in objects.items()}
    for key, value in sorted(result.items()):
        print(f'{key}: {value[0]}, {value[1]}')
