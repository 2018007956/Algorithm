# Solved (26m)
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    cnt = 0
    queue = deque([[x,y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and (campus[nx][ny]=='O' or campus[nx][ny]=='P'):
                visited[nx][ny] = True
                queue.append([nx,ny])
                if campus[nx][ny]=='P':
                    cnt += 1
    return cnt

N, M = map(int, input().split())
campus = []
for i in range(N):
    tmp = input()
    if 'I' in tmp:
        px = i
        py = tmp.index('I')
    campus.append(tmp)

visited = [[False] * M for _ in range(N)]
cnt = bfs(px,py)
if cnt:
    print(cnt)
else:
    print('TT')