# 푸는중
from itertools import product
from collections import deque
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(case):
    global board 
    for x in case:
        q = deque()
        for y in range(h):
            if board[y][x] != 0:
                q.append((x, y))
                break
        else: # 해당 열에 벽돌이 없는 경우
            return False

        bomb_cnt = [0] * w # 각 열별 깨야하는 벽돌 수
        while q:
            x, y = q.popleft()
            power = board[y][x]
            board[y][x] = 0
            bomb_cnt[x] += 1
            for dy, dx in move:
                for i in range(1, power):
                    ny = y + (dy * i)
                    nx = x + (dx * i)
                    if 0 <= ny < h and 0 <= nx < w and board[ny][nx] != 0:
                        if board[ny][nx] > 1:
                            q.append((nx, ny))
                        board[ny][nx] = 0 # (-> 폭발만 0으로 만들고 중력은 boards에 반영안됨)
                        bomb_cnt[nx] += 1

        # 벽돌 깨기
        for j in range(w):
            while bomb_cnt[j] and stacks[j]:
                stacks[j].pop()
                bomb_cnt[j] -= 1
                
        # stacks -> board 재구성
        board = [[0]*w for _ in range(h)]
        for j in range(w):
            for i in range(h):
                try: 
                    board[i][j] = stacks[j][-i]
                except:
                    pass
    return True


T = int(input())
for tc in range(1, T + 1):
    n, w, h = map(int, input().split())
    board_original = [list(map(int, input().split())) for _ in range(h)]

    res = w * h
    all_cases = product(range(w), repeat=n)
    for case in all_cases:
        board = [row[:] for row in board_original] #### 
        stacks = [[] for _ in range(w)]
        for i in range(w):
            for j in range(h-1, -1, -1):
                if board[j][i] != 0:
                    stacks[i].append(board[j][i]) # 밑에서부터 삽입

        if bfs(case): # 잘 동작한 경우
            # 남아있는 벽돌 수 카운트
            print('===')
            for a in stacks:
                print(a)
            
            res = min(res, sum(board[i][j] != 0 for i in range(h) for j in range(w)))

    print(f'#{tc} {res}')