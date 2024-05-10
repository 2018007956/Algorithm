# Solved (37m)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited = [False] * (N+1)
    visited[start] = 0
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x==end:
            return visited[end]
        for y in graph[x]:
            if not visited[y]:
                queue.append(y)
                visited[y] = visited[x] + 1
    
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
num = []
for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        if i!=j:
            tmp += bfs(i, j)
    num.append(tmp)

print(num.index(min(num))+1)