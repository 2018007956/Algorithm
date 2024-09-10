# 풀이 공부
N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        dp[j] = max(dp[j], dp[i]+schedule[i][1])

print(dp[-1])
'''
10:35~05 (30m) 알고리즘을 어떻게 짜야할지 모르겠음
'''