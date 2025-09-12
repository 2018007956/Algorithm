from collections import deque
move = [[], 
        [(-1, 0), (1, 0), (0, -1), (0, 1)], # 1. 상하좌우
        [(0, -1), (0, 1)], # 2.상하
        [(-1, 0), (1, 0)], # 3.좌우
        [(0, -1), (1, 0)], # 4. 상우 
        [(0, 1), (1, 0)], # 5. 하우
        [(0, 1), (-1, 0)],  # 6. 하좌
        [(0, -1), (-1, 0)]] # 7. 상좌

def bfs(y, x):
    global grid, visited, n, m, l
    q = deque()
    q.append((x, y))
    visited[y][x] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        if visited[y][x] == l:
            return cnt

        for dx, dy in move[grid[y][x]]:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] != 0:
                if (-dx, -dy) in move[grid[ny][nx]]: # 양방향 확인 필요
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))
                    cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    res = bfs(r, c)
    print(f'#{tc} {res}')