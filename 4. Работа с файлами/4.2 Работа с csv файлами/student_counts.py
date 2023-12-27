import csv

with open('student_counts.csv', mode='r', encoding='utf-8') as infile, open('sorted_student_counts.csv', mode='w',
                                                                            encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter=',')
    header = reader.fieldnames
    header = header[:1] + sorted(
        sorted(header[1:]), key=lambda x: int(x.split("-")[0])
    )
    print(header)

    writer = csv.DictWriter(outfile, delimiter=',', fieldnames=header, quoting=csv.QUOTE_NONE)
    writer.writeheader()
    writer.writerows(reader)
