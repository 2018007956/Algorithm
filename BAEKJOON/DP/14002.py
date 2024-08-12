# Solved (54m) w/ Search
import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []
prev_index = [-1] * N
for i, x in enumerate(A):
    pos = bisect.bisect_left([a[0] for a in dp], x)
    if pos==len(dp):
        dp.append((x, i))
    else:
        dp[pos] = (x, i)

    if pos > 0:
        prev_index[i] = dp[pos-1][1]

print(len(dp))

# 역추적
res = []
cur = dp[-1][1]
for _ in range(len(dp)):
    res.append(A[cur])
    cur = prev_index[cur]

res.reverse()
print(*res)

'''
9:40~44 (4m) 틀렸습니다

import bisect
dp = []
for x in A:
    pos = bisect.bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x

print(len(dp))
print(*dp)
=>  순서 보장 안됨

반례
13
3 4 5 6 2 3 1 7 4 3 5 6 7
[정답]
6
2 3 4 5 6 7
[출력]
6
1 3 4 5 6 7

10:13~30, 38~45 (24m) 틀렸습니다
    dp = [A[0], 1] 로 개수 카운트 하는 방식으로 구현
    route 업데이트가 올바르지 않으면 잘못된 결과가 나올 수 있음
    route에 value가 아닌 index 필요

~11:11 (26m) 풀이 참고, Solved
'''