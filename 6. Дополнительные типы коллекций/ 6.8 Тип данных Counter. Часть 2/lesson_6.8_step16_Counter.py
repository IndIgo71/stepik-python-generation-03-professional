import sys
from collections import Counter

students = Counter({k: int(v) for k, v in [line.split() for line in sys.stdin.readlines()]})
print(students.most_common()[-2][0])
