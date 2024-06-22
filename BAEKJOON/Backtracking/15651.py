# Solved (5m)
N, M = map(int, input().split())
s = []
def dfs():
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()
dfs()


# Solved (3m)
from itertools import product
N, M = map(int, input().split())
for x in sorted(product(range(1,N+1), repeat=M)):
    print(*x)