# Solved (6m)
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*N for _ in range(N)]
for i in range(N):
    r, g, b = map(int, input().split())

    dp[i][0] = min(dp[i-1][1]+r, dp[i-1][2]+r)
    dp[i][1] = min(dp[i-1][0]+g, dp[i-1][2]+g)
    dp[i][2] = min(dp[i-1][0]+b, dp[i-1][1]+b)

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))

'''
4:36~4:58 (22m) 문제 이해가 안돼서 문제 설명만 찾아봄
RGB 합쳐진게 같지 않아야 한다고 해석해서 문제 접근을 못하고 있었는데
RGB 중 하나를 골라서 칠하는 거였다.
따라서 "색이 같지 않다"는 말은 "같은 색은 칠하지 않는다는 말

~5:23 (25m) 힌트를 얻고 문제를 풀어보려했는데, 예제 답이 왜 그렇게 나오는지 이해 못함&어떻게 풀어야 할지 모르겠어서 답 확인

다음에 다시 도전 -> Solved in 6m
'''