# Solved (1h 11m)
import bisect
N = int(input())
A = list(map(int, input().split()))

dp = []

for x in A:
    # x보다 크거나 같은 최초의 위치
    pos = bisect.bisect_left(dp, x) 
    # dp의 마지막 원소보다 x가 크다면 추가
    if pos == len(dp): 
        dp.append(x)
    else:
        dp[pos] = x

print(len(dp))

'''
dp : O(N^2)
이진 탐색 : O(N log N)
'''