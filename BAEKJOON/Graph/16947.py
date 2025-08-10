import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

# 요구 사항이 “각 정점이 사이클까지 떨어진 거리”이므로, 사이클 정점 전체를 시작점으로 한 멀티소스 BFS가 필요
# 1. 리프(차수 1)부터 제거해서 사이클 정점 찾기
q = deque()
in_cycle = [True] * (n+1)
for i in range(1, n+1):
    if degree[i] == 1:
        q.append(i)
        in_cycle[i] = False

while q:
    u = q.popleft()
    for v in graph[u]:
        if in_cycle[v]:
            degree[v] -= 1
            if degree[v] == 1:
                q.append(v)
                in_cycle[v] = False

# in_cycle[i] == True 인 정점들이 사이클에 속함

# 2. 사이클 정점들을 시작으로 멀티소스 BFS -> 각 정점의 사이클까지 거리
dist = [-1] * (n+1)
q = deque()
for i in range(1, n+1):
    if in_cycle[i]:
        dist[i] = 0
        q.append(i)

while q:
    u = q.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

print(*dist[1:])