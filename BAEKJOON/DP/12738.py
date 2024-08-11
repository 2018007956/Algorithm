# Solved (7m)
import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []

for x in A:
    pos = bisect.bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x
        
print(len(dp))