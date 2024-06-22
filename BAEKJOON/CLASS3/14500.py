# 풀이 공부
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 세로, 가로
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

move = [(0,1), (0,-1), (-1,0), (1,0)] # U, D, L, R

maxValue = 0
def dfs(i, j, dsum, cnt):
    global maxValue
    if cnt==4:
        maxValue = max(maxValue, dsum)
        return
    
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum+board[ni][nj], cnt+1)
            visited[ni][nj] = False

def exec(i, j):
    global maxValue
    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
            t = (n+k)%4 # 012, 123, 230, 301
            ni = i+move[t][0]
            nj = j+move[t][1]
            if 0<=ni<N and 0<=nj<M:
                tmp += board[ni][nj]
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exec(i, j)

print(maxValue)
'''
Ref) https://cijbest.tistory.com/87
n   0 1 2 3
k   0 1 2
n+k 0 1 2 / 1 2 3 / 2 3 4 / 3 4 5
(n+k)%4 0 1 2 / 1 2 3 / 2 3 0 / 3 0 1
'''