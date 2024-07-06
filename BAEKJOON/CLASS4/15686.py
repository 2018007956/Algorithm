# Solved (35m) 
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken_position = [(x,y) for x in range(N) for y in range(N) if city[x][y]==2]
candidate_chicken = list(combinations(chicken_position, M))

move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 1
    
    chicken_length = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if temp[nx][ny]==1:
                    chicken_length += visited[x][y]
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx,ny))
    
    return chicken_length

result = 1e9
for i in range(len(candidate_chicken)):
    temp = [row[:] for row in city]    
    for x in range(N):
        for y in range(N):
            if temp[x][y]==2 and (x,y) not in candidate_chicken[i]:
                temp[x][y]=0
    
    visited = [[False]*N for _ in range(N)]
    length = bfs(candidate_chicken[i])
    result = min(result, length)

print(result)