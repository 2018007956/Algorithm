# Solved (12m)
import sys
import bisect
input = sys.stdin.readline
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
S.sort()

cnt = 0
for _ in range(M):
    test = input().strip()

    idx = bisect.bisect_left(S, test)
    if idx < len(S) and S[idx].startswith(test):
        cnt += 1

print(cnt)