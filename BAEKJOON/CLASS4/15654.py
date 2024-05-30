# Solved (5m)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in permutations(arr, M):
    print(*x)