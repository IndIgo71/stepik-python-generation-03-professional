import sys

sys.stdout.write(str(len(list(filter(lambda l: l.strip().startswith('#'), sys.stdin.readlines())))))
