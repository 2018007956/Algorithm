# https://school.programmers.co.kr/questions/64959
#               R       L      U      D      Stay
directions = ((1,0), (-1,0), (0,1), (0,-1), (0,0))
ans = 1e8
def solution(maze):
    n, m = len(maze), len(maze[0])

    for x in range(n):
        for y in range(m):
            if maze[x][y] == 1:     r_cur = (x, y)
            elif maze[x][y] == 2:   b_cur = (x, y)
            elif maze[x][y] == 3:   r_goal = (x, y)
            elif maze[x][y] == 4:   b_goal = (x, y)

    r_visit, b_visit = [[False] * m for _ in range(n)], [[False] * m for _ in range(n)]
    r_visit[r_cur[0]][r_cur[1]], b_visit[b_cur[0]][b_cur[1]] = True, True

    def out_of_index(x, y):
        return x < 0 or y < 0 or x >= n or y >= m
    
    def visited(visit, goal, x, y):
        return maze[x][y] != goal and visit[x][y]
    
    def duplicated(x1, x2, y1, y2):
        return x1 == x2 and y1 == y2
    
    def crossed(cur1, cur2, next1, next2):
        return cur1 == next2 and cur2 == next1
    
    def dfs(r_cur, b_cur, r_visit, b_visit, cnt):
        global ans
        if r_cur == r_goal and b_cur == b_goal:
            ans = min(ans, cnt)
            return
        
        for d_rx, d_ry in directions:
            rx_next, ry_next = r_cur[0] + d_rx, r_cur[1] + d_ry

            if out_of_index(rx_next, ry_next) or visited(r_visit, 3, rx_next, ry_next) or maze[rx_next][ry_next]==5:
                continue

            r_visit[rx_next][ry_next] = True

            for (d_bx, d_by) in directions:
                if (d_rx, d_ry)==(0,0) and (d_bx, d_by)==(0,0):
                    break
                bx_next, by_next = b_cur[0] + d_bx, b_cur[1] + d_by

                if out_of_index(bx_next, by_next) or visited(b_visit, 4, bx_next, by_next) or maze[bx_next][by_next]==5 \
                    or duplicated(bx_next, rx_next, ry_next, by_next) or crossed(r_cur, b_cur, (rx_next, ry_next), (bx_next, by_next)):
                    continue

                b_visit[bx_next][by_next] = True
                dfs((rx_next, ry_next), (bx_next, by_next), r_visit, b_visit, cnt+1)
                b_visit[bx_next][by_next] = False # 더 이상 주변을 탐색하면서 나아갈 수 없을 때, 이전 상태로 돌아와 다른 방향을 탐색
            r_visit[rx_next][ry_next] = False # 방문한 기록을 없애줌으로써 backtracking을 호출하기 전 상황으로 되돌려줌
    
    dfs(r_cur, b_cur, r_visit, b_visit, 0)
    return 0 if ans == 1e8 else ans

print(solution([[1, 4], [0, 0], [2, 3]]))


'''
백트래킹 (BackTracking)
조건을 통해서 탐색할 상태가 조건에 위배되지 않는지 판별하고, 위배되지 않는 상태만을 추가하여 탐색하는 기법
조건에 부합하지 않으면 이전 수행으로 돌아감, 주로 DFS를 사용
'''