# Solved (26m) w/ search
import sys
from collections import deque 
input = sys.stdin.readline

def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for y in graph[x]:
            if not visited[y]:
                queue.append(y)
                visited[y] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
for e in graph:
    e.sort() #  인접 정점 중 더 작은 번호를 우선 탐색
    
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)