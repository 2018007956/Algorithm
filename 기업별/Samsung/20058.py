# Solved (1h 55m) w/ Search
import sys
from collections import deque
from itertools import chain
input = sys.stdin.readline

def rotate_90(sy, sx, length):
    new_board = [[0] * 2**N for _ in range(2**N)]

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            oy, ox = y-sy, x-sx
            ry, rx = ox, length-oy-1
            new_board[sy+ry][sx+rx] = board[y][x]

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            board[y][x] = new_board[y][x]

move = [(-1,0), (1,0), (0,1), (0,-1)]
def melting_ice():
    to_decrease = []
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            if board[y][x]:
                for dx, dy in move:
                    nx = x+dx
                    ny = y+dy
                    if 0<=ny<2**N and 0<=nx<2**N and board[ny][nx]:
                        cnt += 1

                if cnt < 3:
                    to_decrease.append((x, y))

    for x, y in to_decrease:
        board[y][x] -= 1

def bfs(x, y):
    visited[y][x] = True
    queue = deque([(x, y)])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if 0<=ny<2**N and 0<=nx<2**N and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt


N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

# 파이어스톰
for l in L:
    if l!=0:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                rotate_90(i, j, 2**l)

    # 얼음 녹음
    melting_ice()

print(sum(list(chain.from_iterable(board))))

visited = [[False] * 2**N for _ in range(2**N)]
max_size = 0
for y in range(2**N):
    for x in range(2**N):
        if board[y][x] and not visited[y][x]:
            max_size = max(max_size, bfs(x, y))

print(max_size)
'''
예제 4번부터 답 이상하게 나옴
    **melting_ice() 에서 반복문을 돌면서 board를 바로 수정하다보니 계산에 차질 발생**
    체크 해 놓고 한꺼번에 감소시켜야 함

예제 6번 max_size 값 하나 더 크게 나옴
    x, y index 접근 에러
    if board[x][y]: bfs(x, y)를 아래와 같이 수정
    if board[y][x]: bfs(x, y)

11:20~20, 1:12~44, 52~09 (1h 49m) 시간 초과
    덩어리 탐색이기 때문에 visited를 함수 밖에 정의

~15 (6m) python 시간초과, pypy Solved
'''