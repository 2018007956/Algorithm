# Solved (15m)
from collections import deque
def bfs(maps):
    move = [(-1,0), (1,0), (0,1), (0,-1)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        if y==len(maps)-1 and x==len(maps[0])-1:
            return visited[y][x]
            
        for dx, dy in move:
            ny = y + dy
            nx = x + dx
            if 0<=ny<len(maps) and 0<=nx<len(maps[0]):
                if not visited[ny][nx] and maps[ny][nx]==1:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
    
    return None
    
def solution(maps):
    global visited
    answer = 0
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    result = bfs(maps)
    if result:
        return result
    else:
        return -1