# Solved (27m) w/ Search
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = defaultdict(int)
for a in A:
    for b in B:
        AB[a+b] += 1

cnt = 0
for c in C:
    for d in D:
        if -(c+d) in AB.keys():
            cnt += AB[-(c+d)]
print(cnt)