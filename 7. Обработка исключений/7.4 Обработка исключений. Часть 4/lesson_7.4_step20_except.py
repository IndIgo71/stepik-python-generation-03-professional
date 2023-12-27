import json

file_name = input()
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(data)
        except json.decoder.JSONDecodeError:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')
