# Solved (1h 30m) w/ Search
import sys
from collections import deque
input = sys.stdin.readline
move = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(start):
    water = deque([(y, x) for y in range(R) for x in range(C) if jido[y][x] == '*'])
    hedgehog = deque([next((y, x) for y in range(R) for x in range(C) if jido[y][x] == 'S')])
    
    water_visited = [[-1] * C for _ in range(R)]
    hedgehog_visited = [[-1] * C for _ in range(R)]

    for y, x in water:
        water_visited[y][x] = 0
    y, x = hedgehog[0]
    hedgehog_visited[y][x] = 0
    
    # 물 먼저 움직이도록 BFS
    while water:
        wy, wx = water.popleft()
        for dx, dy in move:
            nwx = wx + dx
            nwy = wy + dy
            if 0<=nwy<R and 0<=nwx<C and water_visited[nwy][nwx]==-1 and jido[nwy][nwx]=='.':
                water_visited[nwy][nwx] = water_visited[wy][wx] + 1
                water.append((nwy,nwx))
                
    while hedgehog:
        hy, hx = hedgehog.popleft()
        if jido[hy][hx] == 'D':
            return hedgehog_visited[hy][hx]
        for dx, dy in move:
            nhx = hx + dx
            nhy = hy + dy
            if 0<=nhy<R and 0<=nhx<C and hedgehog_visited[nhy][nhx]==-1:
                # 물이 퍼지지 않은 곳이거나 고슴도치가 물보다 빨리 도달할 수 있는 경우 이동
                if jido[nhy][nhx] == 'D' or (jido[nhy][nhx] == '.' and (water_visited[nhy][nhx] == -1 or hedgehog_visited[hy][hx] + 1 < water_visited[nhy][nhx])):
                    hedgehog_visited[nhy][nhx] = hedgehog_visited[hy][hx] + 1
                    hedgehog.append((nhy,nhx))

    # 도달할 수 없는 경우
    return "KAKTUS"
                

R, C = map(int, input().split())
jido = [input() for _ in range(R)]
start = [(y, x) for y in range(R) for x in range(C) if jido[y][x]=='*' or jido[y][x]=='S']
print(bfs(start))
'''
12:26~50 (30m) 틀렸습니다
반례
3 4
.D.*
X.S.
X*..
[정답] KAKTUS
[출력] 2
=> 고슴도치 이동하기 전에 물이 먼저 차야됨
    queue 배열에 * 위치가 먼저 들어오도록 처리, for문 안에서도 물 먼저 처리되도록 조건문 순서 신경씀

~1:07, 4:06~21 (32m) 32% 쯤 틀렸습니다
**큐에서 음수값이 먼저 처리되도록 하는 방식만으로는 물이 항상 고슴도치보다 먼저 처리되도록 보장할 수 없다**
물과 고슴도치의 움직임을 큐에 함께 넣고 단순히 값으로 구분하는 경우, 고슴도치가 물보다 먼저 처리되거나 예상하지 못한 순서로 처리될 가능성이 생긴다
물과 고슴도치의 각각의 이동 경로를 별도로 관리하여 물이 먼저 퍼지고 고슴도치가 그다음에 움직이도록 해야 한다
    (y, x)를 물 먼저 처리한다 하더라도, 그 다음에 오는 (ny, nx)가 항상 물이라는 보장 없음

고슴도치 위치는 항상 하나이므로, list로 받는 것 보다 next로 받는게 효율적
    next는 조건을 만족하는 첫 번째 값을 찾는 즉시 반복을 멈추고 반환함

~5:00 (40m) Solved
또 다른 풀이) queue에 고슴도치 위치를 넣어준 후 물 위치 넣어주기
    고슴도치가 이동했더라도 물이 이동할 위치라면 고슴도치를 덮어쓰기 때문
    https://wookcode.tistory.com/167
'''