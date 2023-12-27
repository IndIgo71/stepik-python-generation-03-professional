from itertools import product


def gen_num(n, m):
    alphabet = '0123456789ABCDEF'
    return (''.join(i) for i in product(alphabet[:n], repeat=m))


n, m = int(input()), int(input())
print(*gen_num(n, m), sep=' ')
