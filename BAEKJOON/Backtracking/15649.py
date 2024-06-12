# Solved (3m)
from itertools import permutations
N, M = map(int, input().split())
for x in sorted(permutations(range(1,N+1),M)):
    print(*x)