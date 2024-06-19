# Solved (3m)
from itertools import product
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in product(arr, repeat=M):
    print(*x)