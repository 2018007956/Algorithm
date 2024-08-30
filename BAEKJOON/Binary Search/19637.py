# Solved (10m)
import sys
import bisect
input = sys.stdin.readline
N, M = map(int, input().split())

power = []
level = []
for _ in range(N):
    a, b = input().split()
    power.append(int(b))
    level.append(a)
    
for _ in range(M):
    x = int(input())
    idx = bisect.bisect_left(power, x)
    print(level[idx])