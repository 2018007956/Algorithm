# 풀이 공부
import sys
input = sys.stdin.readline
N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    t, p = schedule[i]
    if i + t <= N:
        # i일에 상담을 하는 것과 상담을 안하는 것 (현상유지) 중 큰 것을 선택
        dp[i] = max(dp[i+t] + p, dp[i+1])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])

'''
* 뒤에서부터 탐색하는 이유

미래의 선택에 따른 이익을 현재에서 고려해야 하는 구조이므로,
미래의 값을 먼저 계산하고 그 값을 사용해서 현재의 값을 결정하는 방식으로 풀어야 함

dp[i]는 i번째 날부터 얻을 수 있는 최대 이익을 의미하고, 이를 계산하려면 i번째 날 이후의 상태를 먼저 알아야 함


* dp 배열 사용
- 상담을 진행하는 경우: i + t일 이후의 최대 이익에 p만큼 더한 값을 고려
- 상담을 진행하지 않는 경우: i + 1일의 최대 이익을 그대로 가져옴
'''