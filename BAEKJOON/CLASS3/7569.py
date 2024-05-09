# Solved (1h 13m) w/ ref 7576
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and box[nz][ny][nx]==0:
                queue.append([nx,ny,nz])
                box[nz][ny][nx] = box[z][y][x] + 1
    
M, N, H = map(int, input().split())
box = [] 
for _ in range(H):
    one_floor = []
    for _ in range(N):
        one_floor.append(list(map(int, input().split())))
    box.append(one_floor)
    
queue = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if box[k][j][i]==1:
                queue.append([i,j,k])

bfs()

flat_box = [element for row in box for col in row for element in col]
print(-1 if 0 in flat_box else max(flat_box)-1)

'''
9:25~10:17 (52m)
예제 2번 1이 인식안됨

12:58~1:19 (21m) 
예제2번은 0으로만 구성되어 있어서 숫자를 조금 다르게 세팅해서 출력해보니
k가 달라져도 똑같은 숫자가 찍힘 -> input이 잘못 들어감. one_floor를 리셋해줘야됨
'''