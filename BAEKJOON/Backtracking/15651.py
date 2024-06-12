# Solved (3m)
from itertools import product
N, M = map(int, input().split())
for x in sorted(product(range(1,N+1), repeat=M)):
    print(*x)