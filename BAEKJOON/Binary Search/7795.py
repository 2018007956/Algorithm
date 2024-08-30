# Solved (5m)
import sys
import bisect
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()
    cnt = 0
    for a in A:
        cnt += bisect.bisect_left(B, a)
    
    print(cnt)