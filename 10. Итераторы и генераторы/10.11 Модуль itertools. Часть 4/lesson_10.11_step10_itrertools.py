from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons.sort(key=lambda person: (person.height, person.name))
grouped = groupby(persons, key=lambda person: person.height)
for group, people in grouped:
    print(f'{group}: {", ".join(map(str, map(lambda person: person.name, people)))}')
