import csv


def csv_columns(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',')
        headers = rows.fieldnames
        columns = dict()
        for row in rows:
            for header in headers:
                columns.setdefault(header, []).append(row[header])

        return columns
