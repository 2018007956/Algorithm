# Solved (32m)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,end):
    queue = deque([x])
    visited[x] = True 
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:  
                queue.append(y)
                visited[y] = True
        
            if y==end:
                return 1

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            graph[i].append(j)
            
result = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        visited = [False]*N
        if bfs(i,j):
            result[i][j]=1
        else:
            result[i][j]=0
    
for i in result:
    print(*i)