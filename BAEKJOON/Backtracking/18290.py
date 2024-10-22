# Solved (57m) w/ Search
move = [(0,1), (0,-1), (1,0), (-1,0)]
def dfs(depth, cur_sum, last_y, last_x):
    global max_sum
    if depth==K:
        max_sum = max(max_sum, cur_sum)
        return

    for y in range(last_y, N):
        for x in range(last_x if y==last_y else 0, M):
            if not visited[y][x]:
                if (0<=y-1 and visited[y-1][x]) or (y+1<N and visited[y+1][x]) or (0<=x-1 and visited[y][x-1]) or (x+1<M and visited[y][x+1]):
                    continue
                visited[y][x] = True
                dfs(depth+1, cur_sum+board[y][x], y, x)
                visited[y][x] = False


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
max_sum = -float('inf')
for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(1, board[y][x], y, x)
        visited[y][x] = False

print(max_sum)
'''
9:08~30 (22m) 틀렸습니다
    max_sum 변수 초기값 잘못 세팅
    move = [(-1,-1), (1,1), (-1,1), (1,-1), (2,0), (-2,0), (0,2), (0,-2)] 
        이렇게 이동하여 인접한 칸을 선택하지 않도록 하려했으나, 
        이 이동방식은 모든 칸을 탐색하지 못함 ex. (2,2) 떨어진 칸을 가려면 (1,1)을 거쳐 가야됨
        따라서 상화좌우 칸들로 이동하면서 인접한 칸에 방문한 적있는지 확인하는 조건을 걸어야 함

~54 (24m) 2% 시간초과
    last_y, last_x를 통해 이전에 방문한 좌표 이후의 좌표만 탐색하도록 수정하여, 같은 좌표를 중복해서 탐색하는 것을 줄임
    y==last_y일때만 last_x에서 시작하고, 다른 행은 0부터 시작해야 함

~05 (11m) Solved
'''