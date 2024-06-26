# another sol
N, M = map(int, input().split())
s = []
def dfs():
    if len(s)==M:
        print(' '.join(map(str, s)))

    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()


# Solved (7m)
N, M = map(int, input().split())
visited = [False] * (N+1)
res = ''

def dfs(res):
    if len(res)==M:
        print(*list(res))

    for i in range(1, N+1):
        if 0<=i<N+1 and not visited[i]:
            visited[i] = True
            dfs(res+str(i))
            visited[i] = False

for x in range(1, N+1):
    visited[x] = True
    dfs(str(x))
    visited[x] = False


# Solved (3m)
from itertools import permutations
N, M = map(int, input().split())
for x in sorted(permutations(range(1,N+1),M)):
    print(*x)