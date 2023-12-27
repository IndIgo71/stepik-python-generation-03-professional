from collections import namedtuple
import pickle

Animal = namedtuple('Animal', 'name family sex color')

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    for animal in data:
        print(f'name: {animal.name}\nfamily: {animal.family}\nsex: {animal.sex}\ncolor: {animal.color}\n')
