# Solved (14m)
import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []
position = []
prev_index = [-1] * N
for i, x in enumerate(A):
    pos = bisect.bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
        position.append(i)
    else:
        dp[pos] = x
        position[pos] = i

    if pos > 0:
        prev_index[i] = position[pos-1]

print(len(dp))

res = []
cur = position[-1]
for _ in range(len(dp)):
    res.append(A[cur])
    cur = prev_index[cur]

res.reverse()
print(*res)

'''
11:47~54 (8m) 1% 시간초과
    bisect.bisect_left를 호출할 때 매번 dp 리스트의 값들로부터 새로운 리스트를 생성하는 부분이 O(N), 전체적으로 O(N^2)의 시간 복잡도 가짐
    dp에 튜플이 아닌 값만 저장

~12:00 (6m) Solved
'''