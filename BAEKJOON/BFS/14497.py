# Solved (30m) w/ Search
import sys
from collections import deque
input = sys.stdin.readline
move = [(-1,0), (1,0), (0,1), (0,-1)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = 0
    while queue:
        x, y = queue.popleft()
        if (x, y) == (x2-1, y2-1):
            return visited[y][x]
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if 0<=ny<N and 0<=nx<M and visited[ny][nx]==-1:
                if classInfo[ny][nx]=='1' or classInfo[ny][nx]=='#':
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))
                else:
                    visited[ny][nx] = visited[y][x]
                    queue.appendleft((nx, ny)) # appendleft()를 통해 0부터 방문할 수 있도록 함


N, M = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
classInfo = [input().rstrip() for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
print(bfs(x1-1, y1-1))