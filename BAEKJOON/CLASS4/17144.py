# Solved (1h 41m)
import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

move = [(0,1), (0,-1), (-1,0), (1,0)]
def spread_dust(A):
    temp = [item[:] for item in A]
    for x in range(R):
        for y in range(C):
            if A[x][y] > 0: # dust exist
                cnt = 0
                spread_amount = A[x][y] // 5
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<R and 0<=ny<C and A[nx][ny]!=-1:
                        temp[nx][ny] += spread_amount
                        cnt += 1
                temp[x][y] -= spread_amount * cnt
    return temp

def air_cleaner_operation(status):
    cleaner_position = [idx for idx, x in enumerate(status) if x[0]==-1][0]
    
    # 공청기 윗쪽 반시계 방향 회전
    # left col (move down)
    for r in range(cleaner_position-2, -1, -1): 
        status[r+1][0] = status[r][0]
    # up row (move left)
    for c in range(C-1):
        status[0][c] = status[0][c+1]
    # right col (move up)
    for r in range(cleaner_position):
        status[r][-1] = status[r+1][-1]
    # down row (move right)
    for c in range(C-2, 0, -1):
        status[cleaner_position][c+1] = status[cleaner_position][c]
    # 공청기에서 나가는 바람
    status[cleaner_position][1] = 0

    # 공청기 아랫쪽 시계 방향 회전
    # left col (move up)
    for r in range(cleaner_position+2, R-1): 
        status[r][0] = status[r+1][0]
    # down row (move left)
    for c in range(C-1):
        status[-1][c] = status[-1][c+1]
    # right col (move down)
    for r in range(R-2, cleaner_position, -1):
        status[r+1][-1] = status[r][-1]
    # up row (move right)
    for c in range(C-2, 0, -1):
        status[cleaner_position+1][c+1] = status[cleaner_position+1][c]
    # 공청기에서 나가는 바람
    status[cleaner_position+1][1] = 0

    return status


while T:
    A = spread_dust(A)
    A = air_cleaner_operation(A)
    T -= 1

total_dust_amount = sum([sum(row) for row in A]) + 2
print(total_dust_amount)

'''
9:57~10:16 (19m),
12:07~44, 49~02 (50m) 공청기 회전 구현 완 
~19 (17m) 먼지 확산 구현 완 
~34 (15m) 공청기 회전 범위 에러 해결 
'''