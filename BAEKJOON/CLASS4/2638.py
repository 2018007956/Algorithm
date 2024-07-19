# Solved (1h 46m)
import sys
from collections import deque
input = sys.stdin.readline
    
def mark_exterior_air(grid, N, M):
    exterior_air = [[False] * M for _ in range(N)]

    # Initialize queue with all exterior borders as starting points
    queue = deque()
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                if grid[i][j] == 0 and not exterior_air[i][j]:
                    queue.append((i, j))
                    exterior_air[i][j] = True

    # BFS to mark all connected exterior air spaces
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and not exterior_air[nx][ny]:
                exterior_air[nx][ny] = True
                queue.append((nx, ny))

    return exterior_air


def two_side_contact(x, y):
    cnt = 0
    for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<M and grid[nx][ny]==0 and exterior_air[nx][ny]:
            cnt += 1
    
    if cnt >= 2:
        return True
    else:
        return False
    

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    cur_cheese_status = [(x,y) for x in range(N) for y in range(M) if grid[x][y]==1]
    if len(cur_cheese_status)==0:
        break
    
    status = [item[:] for item in grid]
    exterior_air = mark_exterior_air(grid, N, M)
    for x, y in cur_cheese_status:
        if status[x][y] == 1 and two_side_contact(x, y):
            status[x][y] = 0
    cnt += 1
    grid = [item[:] for item in status]
    # print('==cnt:',cnt)
    # for x in grid:
    #     print(*x)
print(cnt)

'''
<그림 2>에서 양쪽 옆부분 제거되지 않도록 two_side_contact 체크할 때 안쪽 부분은 체크 안되게 구현해야 함
    => 방법 : 외부 공기 체크하기
    그리고 외곽 부분인지 체크하는 것 대신 외부 공기를 모두 체크하게 되면 내부 공기 확인을 따로 안해도 됨
'''