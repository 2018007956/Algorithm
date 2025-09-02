import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(start):
    q = deque(start)

    while q:
        x, y = q.popleft()
        cnt = 0
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                cnt += 1
                continue
            if 0<=ny<r and 0<=nx<c and board[ny][nx] == '.' and not x_pos[ny][nx]:
                cnt += 1

        if cnt >= 3:
            board[y][x] = '.'


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
x_pos = [[False] * c for _ in range(r)]
start = []
for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            start.append((x, y))
            x_pos[y][x] = True
            
bfs(start)

# print('====')
# for i in range(r):
#     print(''.join(board[i]))

# print('====')
min_r, max_r = r, -1
min_c, max_c = c, -1
for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            min_r = min(min_r, y)
            max_r = max(max_r, y)
            min_c = min(min_c, x)
            max_c = max(max_c, x)
    
for i in range(min_r, max_r+1):
    print(''.join(board[i][min_c:max_c+1]))
'''
### 오답노트 ###
board[:][x] 는 열을 나타내는게 아님
board[:]는 단지 얕은 복사(행 리스트 그대로 복제)이고, 그 다음의 [x]가 행 인덱싱으로 해석됨
-> board[:][c-1-x] 에서 행 범위 벗어나면 IndexError 발생

올바른 열 탐색 방법 : if all(row[col] == '.' for row in board)
'''

'''
반례1) c//2까지만 좌·우를 잘라서, 왼쪽(혹은 오른쪽) 빈 열이 절반을 초과하는 경우
2 10
........XX
........XX
정답 : 
XX
XX
코드 결과 :
왼쪽 자르기 루프가 for x in range(c//2) -> range(5) 까지만 증가
실제 왼쪽 빈 열은 8열인데, 5열만 잘라 min_c=5에서 멈춤
...XX
...XX

반례2) 최소 직사각형 내부에 “빈 행”이 껴 있는 경우
개선) min_r, max_r 도 구해서 행도 자르도록 수정
'''