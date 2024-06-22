# Solved (11m)
arr = []
while True:
    tmp = list(map(int, input().split()))
    if len(tmp)==1 and tmp[0]==0:
        break
    k, S = tmp[0], tmp[1:]
    arr.append(S)

s = []
def dfs(arr, depth):
    if len(s)==6:
        print(*s)
        return

    for i in range(depth, len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
            dfs(arr, i+1)
            s.pop()

for a in arr:
    dfs(a, 0)
    print()


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