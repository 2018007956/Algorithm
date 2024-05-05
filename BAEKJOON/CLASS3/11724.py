# Solved (23m)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, cnt):
    queue = deque([x])
    visited[x] = cnt
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:
                queue.append(y)
                visited[y] = cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
cnt = 1
for x in range(1,N+1):
    if not visited[x]:
        bfs(x, cnt)
        cnt += 1
        
print(len(set(visited))-1)