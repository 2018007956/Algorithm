# Solved (1h)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1]*3 for _ in range(N)] for _ in range(N)]

def dfs(y,x,shape): # shape: 가로 0 / 세로 1 / 대각선 2
    # 이미 계산된 경우 바로 반환
    if dp[y][x][shape] != -1:
        return dp[y][x][shape]

    if y == N-1 and x == N-1:
        return 1
    
    ways = 0

    # 대각선 이동 (어떤 shape이든 다 대각선 이동 가능)
    if y+1<N and x+1<N and grid[y][x+1]==0 and grid[y+1][x+1]==0 and grid[y+1][x]==0:
        ways += dfs(y+1,x+1,2)

    # 가로인 경우
    if shape==0 and x+1<N:
        if grid[y][x+1]==0:
            ways += dfs(y,x+1,0)

    # 세로인 경우
    if shape==1 and y+1<N:
        if grid[y+1][x]==0:
            ways += dfs(y+1,x,1)

    # 대각선인 경우
    if shape==2:
        if x+1<N and grid[y][x+1]==0:
            ways += dfs(y,x+1,0)
        if y+1<N and grid[y+1][x]==0:
            ways += dfs(y+1,x,1) 

    # 현재 상태 결과 저장
    dp[y][x][shape] = ways
    return ways


print(dfs(0,1,0))

'''
파이프의 왼쪽을 기준으로 놓고 탐색하니까 종료 조건이 복잡해짐
파이프의 오른쪽 끝이 N-1, N-1에 도달하는지를 봐야함

11:46~36 (50m) 80몇퍼에서 시간초과
    메모이제이션 적용

~46 (10m) Solved w/ GPT
'''