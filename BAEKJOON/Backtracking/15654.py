# Solved (3m)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []
def dfs():
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        if arr[i] not in s:
            s.append(arr[i])
            dfs()
            s.pop()

dfs()


# Solved (5m)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in permutations(arr, M):
    print(*x)