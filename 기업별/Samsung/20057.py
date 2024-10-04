# Solved (1h 47m) w/ Search
from itertools import chain
# d=0:left / 1:down / 2:right / 3:up
move = [(0,-1), (1,0), (0,1), (-1,0)]
def wind_move(r, c, d): # input : y index & direction
    total_sand_moved = 0

    sand = int(A[r][c] * 0.05)
    if 0<=r+move[d][0]*2<N and 0<=c+move[d][1]*2<N:
        A[r+move[d][0]*2][c+move[d][1]*2] += sand
    total_sand_moved += sand # 칸 밖으로 나간 모래도 반영해줘야 하기 때문에 if문에 포함 X

    if move[d][0]==0: # 가로 이동인 경우 row +-1
        for dr, dc, p in [(1, move[d][1], 0.1), (-1, move[d][1], 0.1), 
                          (1, 0, 0.07), (-1, 0, 0.07), 
                          (2, 0, 0.02), (-2, 0, 0.02), 
                          (1, -move[d][1], 0.01), (-1, -move[d][1], 0.01)]:
            sand = int(A[r][c] * p)
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N:
                A[nr][nc] += sand
            total_sand_moved += sand
    else: # 세로 이동인 경우 col +- 1
        for dr, dc, p in [(move[d][0], 1, 0.1), (move[d][0], -1, 0.1),
                          (0, 1, 0.07), (0, -1, 0.07),
                          (0, 2, 0.02), (0, -2, 0.02),
                          (-move[d][0], 1, 0.01), (-move[d][0], -1, 0.01)]:
            sand = int(A[r][c] * p)
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N:
                A[nr][nc] += sand
            total_sand_moved += sand
    
    if 0<=r+move[d][0]<N and 0<=c+move[d][1]<N:
        A[r+move[d][0]][c+move[d][1]] += A[r][c] - total_sand_moved

    A[r][c] = 0


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def solution():
    r, c = N//2, N//2
    d = 0
    cnt = 0
    length = 1
    while True:
        for _ in range(length):
            r, c = r+move[d][0], c+move[d][1]
            wind_move(r, c, d)
            if r==0 and c==0:
                return
            # print('==', r, c, d)
        d += 1
        d %= 4
        cnt += 1
        if cnt == 2:
            length += 1
            cnt = 0    

prev = sum(chain.from_iterable(A))
solution()
after = sum(chain.from_iterable(A))
print(prev-after)
'''
12:10~1:30 (1h 20m) 
    구현을 다 했는데, 예제 3번부터 오답
    디버깅 너무 어려워서 문제 조건 빠트린게 있나 보는데 모르겠음

10:36~11:03 (27m) 내 코드 틀린 부분 GPT 질문
    alpha값을 A[r][c] - int(A[r][c] * 0.45)로 처리하는데, 여기서 0.45는 분배된 모래의 비율을 뜻하지만, 
    실제 분배된 모래의 양은 각 비율을 int로 처리하면서 소수점 이하가 잘리므로 정확하지 않음

    하나씩 if문으로 범위확인하며 계산해주던 코드를 for문으로 리팩토링
'''