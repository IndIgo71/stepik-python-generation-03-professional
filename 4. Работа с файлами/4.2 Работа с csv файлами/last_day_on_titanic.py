import csv

with open('titanic.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    male_survivors = []
    female_survivors = []
    for row in reader:
        if int(row['survived']) == 1 and float(row['age']) < 18:
            if row['sex'] == 'male':
                male_survivors.append(row['name'])
            else:
                female_survivors.append(row['name'])

    print(*male_survivors, sep="\n")
    print(*female_survivors, sep="\n")
