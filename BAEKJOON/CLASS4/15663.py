# Solved (4m)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
for x in sorted(set(permutations(arr, M))):
    print(*x)