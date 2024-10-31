# Solved (40m) w/ Search
import heapq as hq
move = [(1,0), (-1,0), (0,1), (0,-1)]
def dijkstra():
    q = []
    hq.heappush(q, (board[0][0], 0,0))
    distance[0][0] = 0
    while q:
        cost, x, y = hq.heappop(q)
        if x==N-1 and y==N-1:
            print(f"Problem {cnt}: {distance[y][x]}")
            break

        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                ncost = cost + board[ny][nx]
                if ncost < distance[ny][nx]:
                    distance[ny][nx] = ncost
                    hq.heappush(q, (ncost, nx, ny))


cnt = 1
while True:
    N = int(input())
    if N==0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e8] * N for _ in range(N)]
    dijkstra()
    cnt += 1