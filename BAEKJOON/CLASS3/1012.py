# Solved (45m)
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and ground[nx][ny]==1:
                queue.append([nx,ny])
                visited[nx][ny] = cnt

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    cnt = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ground[i][j]==1:
                bfs(i, j)
                cnt += 1

    flat_list = [element for row in visited for element in row] # 2차원 배열을 1차원 배열로 변환
    if False in flat_list:  print(len(set(flat_list))-1)
    else:   print(len(set(flat_list)))

'''
12:33~1:08 (35m) 틀렸습니다
반례
1
1 1 1
0 0
[정답] 1
[출력] 0
최종 visited 배열에 False가 없는 경우도 있음
-> if else 로 처리
'''