# Solved (10m)
import sys
from collections import defaultdict
input = sys.stdin.readline

N, C = map(int, input().split())
messages = list(map(int, input().split()))

sort_by_frequency = defaultdict(int)
for x in messages:
    sort_by_frequency[x] += 1

for k, v in sorted(sort_by_frequency.items(), key=lambda x:x[1], reverse=True):
    for _ in range(v):
        print(k, end=' ')