# Solved (1h 16m)
from collections import deque
N = int(input())
K = int(input())
apple = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input()) # 뱀의 방향 변환 횟수
direction = deque([tuple(input().split()) for _ in range(L)])

# board 구성
board = [[0] * N for _ in range(N)]
board[0][0] = 1 # snake start pos
for r, c in apple:
    board[r-1][c-1] = 2

# Game Start
snake_body = deque([[0, 0]])
time = 0
change_d = [(0,1), (1,0), (0,-1), (-1,0)] # -> Right / <- Left
cur_d_idx = 0
while True:
    r, c = snake_body[-1]
    nr, nc = r+change_d[cur_d_idx][0], c+change_d[cur_d_idx][1]
    time += 1
    # finish condition 1) face the wall
    if not (0 <=nr<N and 0<=nc<N):
        print(time)
        break
    # finish condition 2) face snake body
    if [nr, nc] in snake_body:
        print(time)
        break

    # 방향 전환
    if direction and direction[0][0]==str(time):
        _, d = direction.popleft()
        if d=='D':
            cur_d_idx += 1
            cur_d_idx %= 4
        else: # 'L'
            cur_d_idx -= 1
            cur_d_idx %= 4

    # 사과 먹기
    if board[nr][nc]==2:
        board[nr][nc] = 1
    else:
        snake_body.popleft()

    snake_body.append([nr, nc])

'''
8:31~9:40 (1h 11m) 틀렸습니다
    게시판 확인) 먹은 사과를 치워줘야 함

~45 (5m) Solved
'''
