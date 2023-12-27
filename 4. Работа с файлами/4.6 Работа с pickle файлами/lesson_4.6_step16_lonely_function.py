import pickle
import sys

file_name = input()
args = list(map(str.strip, sys.stdin.readlines()))

with open(file_name, mode='rb') as file:
    fnc = pickle.load(file)
    print(fnc(*args))
