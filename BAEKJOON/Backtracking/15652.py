# Solved (2m)
N, M = map(int, input().split())
s = []
def dfs(x):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(x, N+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)


# Solved (4m)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
for x in combinations_with_replacement(range(1,N+1), M):
    print(*x)