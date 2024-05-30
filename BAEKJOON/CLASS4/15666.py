# Solved (7m)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
for x in combinations_with_replacement(arr, M):
    print(*x)