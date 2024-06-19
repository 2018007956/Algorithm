# Solved (3m)
from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in sorted(combinations(arr, M)):
    print(*x)