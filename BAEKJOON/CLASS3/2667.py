# Solved (27m)
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=N-1 and 0<=ny<=N-1 and not visited[nx][ny] and jido[nx][ny]==1:
            dfs(nx, ny)

N = int(input())
jido = []
for _ in range(N):
    jido.append(list(map(int,list(input().strip()))))
    
visited = [[False]*N for _ in range(N)]
danji = []
for x in range(N):
    for y in range(N):
        if not visited[x][y] and jido[x][y]==1:
            cnt = 0
            dfs(x, y)
            danji.append(cnt)

print(len(danji))
for n in sorted(danji):
    print(n)