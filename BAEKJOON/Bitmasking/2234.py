# 풀이 공부 (2h)
import sys
from collections import deque
input = sys.stdin.readline
move = [(-1,0), (0,-1), (1,0), (0,1)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    room = 1
    while queue:
        x, y = queue.popleft()
        wall = 1
        # (서, 북, 동, 남)에 대해 벽이 있는지 확인
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if (board[y][x] & wall) != wall: # 해당 방향에 벽이 없음
                if 0<=ny<M and 0<=nx<N and not visited[ny][nx]:
                    room += 1
                    queue.append((nx, ny))
                    visited[ny][nx] = True
            wall *= 2

    return room


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

roomCnt = 0
maxRoom = 0
delRoom = 0

for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            roomCnt += 1
            maxRoom = max(maxRoom, bfs(x, y))

print(roomCnt)
print(maxRoom)

for y in range(M):
    for x in range(N):
        wall = 1
        while wall < 9:
            if wall & board[y][x]:
                visited = [[False] * N for _ in range(M)]
                board[y][x] -= wall
                delRoom = max(delRoom, bfs(x, y))
                board[y][x] += wall
            wall *= 2

print(delRoom)
'''
IDEA
1. (서, 북, 동, 남) 방향 순서대로 move를 구성하고, wall을 *2 씩 해주며 4방향 탐색
2. board[y][x]를 wall (1, 2, 4, 8)과 & 연산을 하여 해당 방향으로 벽이 있는지를 확인함
'''