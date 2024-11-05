# Solved (37m) w/ Search
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if i==0 or j==0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        res = max(res, dp[i][j])
        
print(res*res)
'''
11:06~28 (22m) 3% 런타임에러 (ValueError)
    input()을 int로 그대로 받아서 젤 앞이 0인 경우 index 접근 에러 발생

~33, 42~6 (9m) 3% 틀렸습니다
    가장 큰 정사각형의 넓이를 구하는 것이므로, dp[i][j]가 현재 위치에서 가장 큰 정사각형의 한 변의 길이를 의미하도록 구성

~52 (6m) Solved
'''