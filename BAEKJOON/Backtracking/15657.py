# Solved (1m)
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
def dfs(depth):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(depth,N):
        s.append(arr[i])
        dfs(i) 
        s.pop()
            
dfs(0)


# Solved (5m)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in combinations_with_replacement(arr, M):
    print(*x)