# Solved (8m)
from itertools import combinations
arr = []
while True:
    tmp = list(map(int, input().split()))
    if len(tmp)==1 and tmp[0]==0:
        break
    k, S = tmp[0], tmp[1:]
    arr.append(S)

for S in arr:
    for x in combinations(S, 6):
        print(*x)
    print()