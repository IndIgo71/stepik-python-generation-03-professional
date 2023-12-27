import sys

lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    sys.stdout.write(line[::-1] + '\n')
