obj = eval(input())
if isinstance(obj, list):
    print(obj[-1])
elif isinstance(obj, tuple):
    print(obj[0])
elif isinstance(obj, set):
    print(len(obj))
