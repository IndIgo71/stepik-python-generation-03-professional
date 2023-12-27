import csv

with open('wifi.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    districts = dict()
    for row in reader:
        districts[row['district']] = districts.get(row['district'], 0) + int(row['number_of_access_points'])

    for k, v in sorted(districts.items(), key=lambda x: (-x[1], x[0])):
        print(f'{k}: {v}')
