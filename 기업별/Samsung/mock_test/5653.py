# 푸는중
from collections import deque
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y):
    global grid, n, m, k
    q = deque()
    q.append((x, y))
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    grid_x2_origin = [[val*2 for val in row] for row in grid]
    grid_x2 = [[val*2 for val in row] for row in grid]
    
    # 칸의 값을 -1씩 감소
    for _ in range(k):
        cur_n = len(grid_x2)
        cur_m = len(grid_x2[0])
        for i in range(cur_n):
            for j in range(cur_m):
                if grid_x2[i][j] > 0:
                    grid_x2[i][j] -= 1
                
                # 0되면 상하좌우 확장
                if grid_x2[i][j] == 0:
                    for dx, dy in move:
                        nx = j + dx
                        ny = i + dy

                        if ny < 0 or ny >= cur_n or nx < 0 or nx >= cur_m:
                            # 그리드 확장
                            if ny < 0:  # 위쪽 확장
                                grid_x2.insert(0, [0] * cur_m)
                                cur_n += 1
                                i += 1  # 인덱스 보정
                                ny = 0
                            elif ny >= cur_n:  # 아래쪽 확장
                                grid_x2.append([0] * cur_m)
                                cur_n += 1
                            
                            if nx < 0:  # 왼쪽 확장
                                for row in grid_x2:
                                    row.insert(0, 0)
                                cur_m += 1
                                j += 1  # 인덱스 보정
                                nx = 0
                            elif nx >= cur_m:  # 오른쪽 확장
                                for row in grid_x2:
                                    row.append(0)
                                cur_m += 1
                                
                        # 확장된 그리드에 값 넣기
                        grid_x2[ny][nx] = max(grid_x2[ny][nx], grid_x2_origin[i][j])
                    
                    grid_x2_origin = [row[:] for row in grid_x2]



    print(grid_x2)
    print(f'#{tc} {sum(grid_x2[i][j] > 0 for i in range(n) for j in range(m))}')