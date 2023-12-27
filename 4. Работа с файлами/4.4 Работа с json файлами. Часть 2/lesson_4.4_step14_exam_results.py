import csv
import json
from datetime import datetime

pattern = '%Y-%m-%d %H:%M:%S'
with (open('exam_results.csv', 'r', encoding='utf-8') as infile,
      open('best_scores.json', 'w', encoding='utf-8') as outfile):
    reader = csv.DictReader(infile, delimiter=',')
    student_results = {}
    for row in reader:
        student_results.setdefault((row['name'], row['surname'], row['email']), dict()).setdefault(
            datetime.strptime(row['date_and_time'], pattern), int(row['score']))

    best_student_results = {key: max(value.items(), key=lambda x: (x[1], x[0])) for key, value in
                            student_results.items()}
    result = [
        {'name': key[0], 'surname': key[1], 'best_score': value[1], 'date_and_time': value[0].strftime(pattern),
         'email': key[2]}
        for key, value in best_student_results.items()]

    json.dump(sorted(result, key=lambda r: r['email']), outfile, ensure_ascii=False, indent=3)
