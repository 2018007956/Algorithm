# Solved (1m)
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
def dfs():
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        s.append(arr[i])
        dfs() 
        s.pop()
            
dfs()


# Solved (3m)
from itertools import product
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in product(arr, repeat=M):
    print(*x)