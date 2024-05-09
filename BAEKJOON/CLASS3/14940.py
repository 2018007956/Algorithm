# Solved (30m)
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
one_idx = []
def bfs(x, y):
    queue = deque([[x,y]])
    jido[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and jido[nx][ny]==1:
                jido[nx][ny] = jido[x][y] + 1
                queue.append([nx, ny])
                if jido[nx][ny]==1:
                    one_idx.append([nx,ny]) # jido[x][y]==2일때 바뀌기 때문에 위치 save
    

n, m = map(int, input().split())
jido = []
for _ in range(n):
    jido.append(list(map(int, input().rstrip().split())))

start_find = False
for i in range(n):
    for j in range(m):
        if jido[i][j]==2:
            bfs(i, j)
            start_find = True
            break
    if start_find:  break

## Post processing
for i in range(n):
    for j in range(m):
        if jido[i][j]==1:
            jido[i][j]=-1 # 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력

for x, y in one_idx:
    jido[x][y] = 1 

## Print
for i in jido:
    print(' '.join(map(str, i)))