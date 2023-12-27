import csv


def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as infile, open('condensed.csv', 'w', encoding='utf-8',
                                                               newline='') as outfile:
        context = csv.reader(infile)
        objects = {}

        for obj, attr, value in context:
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value

        writer = csv.DictWriter(outfile, fieldnames=objects[obj])
        writer.writeheader()
        writer.writerows(objects.values())
