# Solved (1h 49m) w/ GPT
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(start):
    queue = deque([start])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    fish = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and status[nx][ny] <= baby_shark_size:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if 0 < status[nx][ny] < baby_shark_size:
                    fish.append((visited[x][y], nx, ny))
                    
    if fish:
        fish.sort(key=lambda x: (x[0], x[1], x[2]))
        return fish[0]
    else:
        return None 
        

baby_shark_size = 2
eat = 0
time = 0
baby_shark_position = [(x,y) for x in range(N) for y in range(N) if status[x][y]==9][0]
status[baby_shark_position[0]][baby_shark_position[1]] = 0

while True:
    target = bfs(baby_shark_position)
    if target is None:
        break

    dist, x, y = target
    time += dist
    status[x][y] = 0
    baby_shark_position = (x,y)
    eat += 1
    if eat == baby_shark_size:
        baby_shark_size += 1
        eat = 0

print(time)

'''
5:24~55, 10:07~11:02 (1h 26m) 예제 4까지는 맞는데, 5, 6이 틀리는 상황
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

def bfs(start):
    queue = deque([start])
    status[start[0]][start[1]] = 0 # 이동 가능하도록
    eat = 0
    baby_shark_size = 2
    time = 0
    while queue:
        x, y = queue.popleft()
        eat_candidate = [[abs(nx-x)+abs(ny-y), (nx,ny)] for nx in range(N) for ny in range(N) if 0<status[nx][ny]<baby_shark_size]
        if eat_candidate:
            eat_candidate.sort(key=lambda x : (x[0], x[1][0], x[1][1])) # 우선순위: 위 > 왼쪽 > 나머지
            dist, (nx, ny) = eat_candidate[0]
            queue.append((nx,ny))
            status[nx][ny] = 0
            eat += 1
            time += dist
            if eat == baby_shark_size:
                baby_shark_size += 1
                eat = 0
        
    if eat==0 and baby_shark_size==2:
        print(0)
    else:
        print(time)

baby_shark_position = [(x,y) for x in range(N) for y in range(N) if status[x][y]==9][0]
eated = [[False] * N for _ in range(N)]
bfs(baby_shark_position)


~11:25 (23m) w/ GPT
    candidate로 미리 받아놓지 말고 bfs로 한칸씩 이동하며 거리 계산 & 먹을 수 있는 것들 담아서 반환
    그걸 받아서 baby_shark_position 이동시키고 다시 bfs 돌리기 반복

    
 * 물고기 위치를 미리 구해 놓고 탐색하는 내 첫 번째 코드 틀린 로직 찾기
    => 틀린 이유 : "중간에 자기보다 큰 물고기가 있으면 돌아서 가기 때문에 최단 경로라고 해서 abs 절대값으로 구하는게 아님"
        결국 정답 코드처럼 한 칸씩 이동하며 거리 계산해줘야 함
'''