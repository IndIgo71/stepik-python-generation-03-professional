from string import ascii_lowercase

alphabet = dict(zip(ascii_lowercase, input()))
print(input().lower().translate(str.maketrans(alphabet)))
