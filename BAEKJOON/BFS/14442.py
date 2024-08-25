# Solved (47m)
import sys
from collections import deque
input = sys.stdin.readline
move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[y][x][0] = 1
    while queue:
        x, y, break_cnt = queue.popleft()
        if (x, y) == (M-1, N-1):
            return visited[y][x][break_cnt]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M:
                if jido[ny][nx]=='1' and break_cnt<K and not visited[ny][nx][break_cnt+1]:
                    visited[ny][nx][break_cnt+1] = visited[y][x][break_cnt] + 1
                    queue.append((nx, ny, break_cnt+1))

                if jido[ny][nx]=='0' and not visited[ny][nx][break_cnt]:
                    visited[ny][nx][break_cnt] = visited[y][x][break_cnt] + 1
                    queue.append((nx, ny, break_cnt))
    
    return -1

N, M, K = map(int, input().split())
jido = [input() for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))

# for c in visited:
#     print(*c)
'''
10:43~11:09 (26m) 시간 초과

~30 (21m) Solved w/ PyPy3
    not visited[ny][nx][break_cnt+1] 추가해주니 해결
'''