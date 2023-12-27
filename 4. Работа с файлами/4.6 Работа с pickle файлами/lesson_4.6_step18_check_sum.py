import pickle

filename = input()
checksum = int(input())
with open(filename, mode='rb') as file:
    data = pickle.load(file)
    lst = list(filter(lambda x: isinstance(x, int), data))
    if isinstance(data, list):
        total = min(lst, default=0) * max(lst, default=0)
    elif isinstance(data, dict):
        total = sum(lst)

    if total == checksum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')
