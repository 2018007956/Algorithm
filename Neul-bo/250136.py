from collections import deque
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(land, x, y, cid):
    q = deque([(x, y)])
    quantity = 1
    visited[y][x] = cid
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<n and 0<=nx<m and visited[ny][nx]==-1 and land[ny][nx]==1:
                visited[ny][nx] = cid
                q.append((nx, ny))
                quantity += 1
    
    sizes[cid] = quantity

def solution(land):
    global visited, n, m, sizes
    n, m = len(land), len(land[0])
    visited = [[-1] * m for _ in range(n)]
    sizes = {}
    cid = -1
    
    # 1) BFS로 컴포넌트 라벨링
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and visited[y][x] == -1:
                cid += 1
                bfs(land, x, y, cid)
                
    # 2) 열별로 중복 없는 컴포넌트 합산
    total_oil = 0
    # column 탐색
    for x in range(m):
        seen = set()
        cur_oil = 0
        for y in range(n):
            if land[y][x]==1 and visited[y][x]!=-1:
                c = visited[y][x]
                if c not in seen:
                    cur_oil += sizes[c]
                    seen.add(c)
        # print(x+1, ':', cur_oil)
        # print(seen)
        total_oil = max(total_oil, cur_oil)
    return total_oil