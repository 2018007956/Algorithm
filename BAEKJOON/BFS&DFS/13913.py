# Solved (18m)
from collections import deque
def bfs(x):
    queue = deque([x])
    visited[x] = 0
    while queue:
        x = queue.popleft()
        if x==K:
            print(visited[x])
            break

        for i in [x*2,x+1,x-1]:
            if 0<=i<=100000 and visited[i]==-1:
                queue.append(i)
                route[i] = x
                visited[i] = visited[x] + 1

N, K = map(int, input().split())
visited = [-1] * 100001
route = [-1] * 100001
bfs(N)

# trace
path = [K]
cur = K
while cur != N:
    cur = route[cur]
    path.append(cur)

print(*reversed(path))